#!/usr/bin/env python3
"""Score thesis.md. Agent never edits this file.

score = sum over claims of (grounding_gate * (1 + innovation) - CLAIM_COST) - words/200

grounding_gate: 0 or 1 from code checks (every cited source URL resolves, every
quote in the source entry appears verbatim in the fetched page) AND judge
grounding >= 1. innovation: judge novelty+mechanism+specificity+consequence+tension,
median of 3 judge samples. Judge results cached by hash of (claim text, passages).

usage: python3 eval/score.py [--json] [--no-cache]
"""
import argparse, shutil
import hashlib, html, json, os, re, statistics, subprocess, sys, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "eval", ".cache")
JUDGE_MODEL = os.environ.get("JUDGE_MODEL", "sonnet")
SAMPLES = 3
WORDS_PER_POINT = 200
CLAIM_COST = 4  # every live claim costs this; an add must earn more than its existence
os.makedirs(CACHE, exist_ok=True)


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def cache_get(key):
    p = os.path.join(CACHE, key)
    return json.loads(read(p)) if os.path.exists(p) else None


def cache_put(key, val):
    with open(os.path.join(CACHE, key), "w") as f:
        json.dump(val, f)


def norm(s):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s))
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def fetch(url):
    key = "page-" + hashlib.sha1(url.encode()).hexdigest()
    c = cache_get(key)
    if c is not None:
        return c
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 agent-research scorer"})
        with urllib.request.urlopen(req, timeout=30) as r:
            body = r.read(5_000_000).decode("utf-8", "replace")
        out = {"ok": True, "text": norm(body)}
    except Exception as e:  # noqa
        out = {"ok": False, "text": "", "err": str(e)[:200]}
    cache_put(key, out)
    return out


def parse_sources():
    out = {}
    d = os.path.join(ROOT, "sources")
    for fn in os.listdir(d):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        t = read(os.path.join(d, fn))
        m = re.search(r"^URL:\s*(\S+)", t, re.M)
        ty = re.search(r"^Type:\s*(\w+)", t, re.M)
        qsec = t.split("Quotes:", 1)[1] if "Quotes:" in t else ""
        quotes = [m.group(1) for m in re.finditer(r'^- [^"\n]*"([^"\n]{12,}?)"', qsec, re.M)]
        entry = {"url": m.group(1) if m else None, "quotes": [q.strip() for q in quotes],
                 "type": (ty.group(1).lower() if ty else "secondary")}
        out[slug] = entry
        out[re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slug)] = entry  # cite with or without date prefix
    return out


def parse_claims():
    t = read(os.path.join(ROOT, "thesis.md"))
    claims = []
    for m in re.finditer(r"^## (C\d+)\.\s*(.+?)\n(.*?)(?=^## C\d+\.|\Z)", t, re.M | re.S):
        cid, title, body = m.group(1), m.group(2).strip(), m.group(3)
        conf = re.search(r"^Confidence:\s*(\w+)", body, re.M)
        if conf and conf.group(1) == "retired":
            continue
        rests = re.search(r"^Rests on:.*$", body, re.M)
        slugs = re.findall(r"(?<!\[)\[([a-z0-9][a-z0-9-]+)\](?!\])", rests.group(0)) if rests else []
        text = title + "\n" + re.sub(r"^(Confidence|Rests on|Counter-evidence|History):.*$", "", body, flags=re.M).strip()
        claims.append({"id": cid, "text": text, "slugs": slugs, "words": len(t.split())})
    return claims, len(t.split())


VERIFIED = os.path.join(ROOT, "eval", "verified-quotes.tsv")  # tracked: slug<TAB>sha1(norm quote) once a quote has been seen verbatim


def load_verified():
    out = set()
    if os.path.exists(VERIFIED):
        for line in read(VERIFIED).splitlines():
            f = line.split("\t")
            if len(f) >= 2:
                out.add((f[0], f[1]))
    return out


def mark_verified(slug, q):
    key = (slug, hashlib.sha1(norm(q).encode()).hexdigest())
    if key not in _VER:
        _VER.add(key)
        with open(VERIFIED, "a") as f:
            f.write(f"{key[0]}\t{key[1]}\n")


_VER = load_verified()


def ground_code(claim, sources):
    """Returns (gate 0/1, passages, reasons). A quote that was verified verbatim on an earlier run
    still passes when the host is temporarily down or blocking (gate noise was 4+ points per flip);
    the reason list notes it so the verifier can re-check later."""
    if not claim["slugs"]:
        return 0, [], ["no sources cited"]
    passages, reasons = [], []
    for s in claim["slugs"]:
        src = sources.get(s)
        if not src:
            reasons.append(f"{s}: no source entry"); continue
        if not src["url"]:
            reasons.append(f"{s}: no URL"); continue
        if not src["quotes"]:
            reasons.append(f"{s}: no quotes"); continue
        page = fetch(src["url"])
        for q in src["quotes"]:
            key = (s, hashlib.sha1(norm(q).encode()).hexdigest())
            if page["ok"] and norm(q) in page["text"]:
                passages.append(f"[{s}] {q}"); mark_verified(s, q)
            elif not page["ok"] and key in _VER:
                passages.append(f"[{s}] {q}")  # previously verified; host down now
            elif not page["ok"]:
                reasons.append(f"{s}: fetch failed {page.get('err','')} and quote never verified")
            else:
                reasons.append(f"{s}: quote not found verbatim: {q[:60]}")
    gate = 1 if passages and not reasons else 0
    return gate, passages, reasons


DIMS = ["grounding", "novelty", "mechanism", "specificity", "consequence", "tension", "evidence", "reach"]
INNOV = ["novelty", "mechanism", "specificity", "consequence", "tension", "evidence", "reach"]


def judge(claim, passages, question, rubric, others="", samples=None):
    samples = samples or SAMPLES
    key = "judge-" + hashlib.sha1((JUDGE_MODEL + question + claim["text"] + "\n".join(passages) + rubric + others + str(samples)).encode()).hexdigest()
    c = cache_get(key)
    if c is not None:
        return c
    prompt = (rubric + "\n\nRESEARCH QUESTION:\n" + question + "\n\nOTHER CLAIMS IN THE THESIS (titles):\n" + others
              + "\n\nCLAIM:\n" + claim["text"]
              + "\n\nVERIFIED PASSAGES:\n" + "\n".join(passages) + "\n\nJSON:")
    results = []
    for _ in range(samples):
        try:
            r = subprocess.run(["claude", "-p", "--model", JUDGE_MODEL, "--output-format", "json"],
                               input=prompt, capture_output=True, text=True, timeout=180)
            if r.returncode:
                raise RuntimeError("Judge CLI exited with an error; check CLI authentication and model access")
            txt = json.loads(r.stdout).get("result", "")
            j = json.loads(re.search(r"\{.*\}", txt, re.S).group(0))
            results.append(j)
        except Exception as e:  # noqa
            results.append({"err": str(e)[:100]})
    dims = DIMS
    good = [r for r in results if all(type(r.get(d)) is int and 0 <= r[d] <= 2 for d in dims)]
    if len(good) < samples // 2 + 1:
        raise RuntimeError("Judge returned too few valid samples; no score was cached")
    out = {d: statistics.median(int(r[d]) for r in good) for d in dims}
    out["note"] = good[0].get("note", "")
    out["samples"] = results
    cache_put(key, out)
    # tracked judgement log so judge consistency can be measured across workers
    try:
        import datetime as _dt
        with open(os.path.join(ROOT, "judge-log.tsv"), "a") as f:
            f.write("\t".join([_dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M"), claim.get("id", "?"),
                               json.dumps([{d: r.get(d) for d in dims} for r in good])]) + "\n")
    except Exception:
        pass
    return out


THIN_CAP = 8  # innovation cap for a claim the reviewer last called thin


def load_verdicts():
    """eval/verdicts.tsv written by worker E: review<TAB>claim<TAB>verdict<TAB>reason. Latest review wins."""
    p = os.path.join(ROOT, "eval", "verdicts.tsv")
    out = {}
    if not os.path.exists(p):
        return out
    for line in read(p).splitlines():
        f = line.split("\t")
        if len(f) < 3 or f[0].startswith("#") or f[0] == "review":
            continue
        rev, cid, verdict = f[0].strip(), f[1].strip(), f[2].strip().lower()
        reason = f[3].strip() if len(f) > 3 else ""
        if cid not in out or rev >= out[cid]["review"]:
            out[cid] = {"review": rev, "verdict": verdict, "reason": reason}
    return out


TITLES = os.path.join(ROOT, "eval", "verdict-titles.tsv")  # tracked: review<TAB>claim<TAB>sha1(title) at first scoring after the verdict


def verdict_applies(v, cid, title):
    """A thin/retire verdict is pinned to the claim title it was given on. A wholesale rewrite
    (new title) escapes the cap; the next review re-labels it. (Review 0003: rebuilt C9 stayed capped.)"""
    if v["verdict"] not in ("thin", "retire"):
        return True
    h = hashlib.sha1(title.strip().encode()).hexdigest()
    rows = {}
    if os.path.exists(TITLES):
        for line in read(TITLES).splitlines():
            f = line.split("\t")
            if len(f) >= 3:
                rows[(f[0], f[1])] = f[2]
    key = (v["review"], cid)
    if key not in rows:
        with open(TITLES, "a") as f:
            f.write(f"{key[0]}\t{key[1]}\t{h}\n")
        return True
    return rows[key] == h


def exemplars(verdicts):
    """Reviewer's taste as examples for the judge: latest 3 thin and 3 real, with reasons."""
    thin = [(c, v) for c, v in verdicts.items() if v["verdict"] == "thin" and v["reason"]]
    real = [(c, v) for c, v in verdicts.items() if v["verdict"] == "real" and v["reason"]]
    thin.sort(key=lambda x: x[1]["review"], reverse=True); real.sort(key=lambda x: x[1]["review"], reverse=True)
    if not thin and not real:
        return ""
    s = "\n\nTHE HUMAN-STANDARD REVIEWER'S RECENT VERDICTS (calibrate to these):\n"
    for c, v in real[:3]:
        s += f"- {c} was judged a REAL idea: {v['reason']}\n"
    for c, v in thin[:3]:
        s += f"- {c} was judged THIN or gamed: {v['reason']}\n"
    return s


def check_local():
    """Check source citations without fetching pages or invoking the judge."""
    sources = parse_sources()
    claims, _ = parse_claims()
    errors = []
    for claim in claims:
        if not claim["slugs"]:
            errors.append(f"{claim['id']}: no source citations")
        for slug in claim["slugs"]:
            source = sources.get(slug)
            if source is None:
                errors.append(f"{claim['id']}: missing source {slug}")
            elif not source["url"] or not source["url"].startswith(("https://", "http://")) or not source["quotes"]:
                errors.append(f"{claim['id']}: source {slug} needs a public URL and quotations")
    if errors:
        raise RuntimeError("\n".join(errors))
    print(f"Local thesis check passed: {len(claims)} live claims; citations resolve. No network or model calls.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate local files without network or model calls")
    parser.add_argument("--json", action="store_true", help="Print live evaluation as JSON")
    parser.add_argument("--focus", metavar="ID", help="Use five samples for a selected claim or scenario")
    parser.add_argument("--no-cache", action="store_true", help="Clear local evaluation caches")
    args = parser.parse_args()
    if args.check:
        check_local()
        return
    if shutil.which("claude") is None:
        parser.error("Live evaluation requires an installed and authenticated Claude CLI; use --check for offline validation")
    if "--no-cache" in sys.argv:
        for f in os.listdir(CACHE):
            os.remove(os.path.join(CACHE, f))
    question = read(os.path.join(ROOT, "question.md"))
    verdicts = load_verdicts()
    rubric = read(os.path.join(ROOT, "eval", "rubric.md")) + exemplars(verdicts)
    sources = parse_sources()
    claims, words = parse_claims()
    total, rows = 0.0, []
    for c in claims:
        gate, passages, reasons = ground_code(c, sources)
        j = {d: 0 for d in DIMS} | {"note": "; ".join(reasons)}
        if gate:
            others = "\n".join(f"{o['id']}. {o['text'].splitlines()[0]}" for o in claims if o["id"] != c["id"])
            # --focus Cn: the claim being edited this iteration gets 5 samples instead of 3,
            # so keep/revert decisions near the 0.5 bar rest on less noise (review 0003, D5).
            focus = sys.argv[sys.argv.index("--focus") + 1] if "--focus" in sys.argv and sys.argv.index("--focus") + 1 < len(sys.argv) else None
            j = judge(c, passages, question, rubric, others, samples=5 if focus == c["id"] else None)
            gate = 1 if j["grounding"] >= 1 else 0
        # evidence is capped by the strongest cited source's declared Type: a press release
        # or secondary summary of a study cannot score like the study itself.
        types = {sources[s]["type"] for s in c["slugs"] if s in sources}
        ecap = 2 if types & {"standard", "primary"} else (1 if types else 0)
        j["evidence"] = min(j["evidence"], ecap)
        innov = sum(j[d] for d in INNOV)
        v = verdicts.get(c["id"])
        if v and not verdict_applies(v, c["id"], c["text"].splitlines()[0]):
            v = None  # title rewritten since the verdict; cap lifted until the next review
        if v and v["verdict"] == "thin" and innov > THIN_CAP:
            j["note"] = f"reviewer {v['review']} called this thin: {v['reason'][:60]} | " + j.get("note", "")
            innov = THIN_CAP
        if v and v["verdict"] == "retire":
            j["note"] = f"reviewer {v['review']} said retire: {v['reason'][:60]} | " + j.get("note", "")
            innov = 0
        s = gate * (1 + innov) - CLAIM_COST
        total += s
        rows.append({"id": c["id"], "gate": gate, "score": s, **{k: j[k] for k in j if k != "samples"}})
    penalty = words / WORDS_PER_POINT
    total -= penalty
    nets = sorted(r["score"] for r in rows)
    median = nets[len(nets) // 2] if nets else 0
    out = {"score": round(total, 2), "words": words, "penalty": round(penalty, 2), "median_net": median,
           "add_bar": median - 1, "claims": rows}
    if "--json" in sys.argv:
        print(json.dumps(out, indent=1))
    else:
        for r in rows:
            print(f"{r['id']:>5} gate={r['gate']} score={r['score']:>2} g={r['grounding']} n={r['novelty']} m={r['mechanism']} s={r['specificity']} c={r['consequence']} t={r['tension']} e={r['evidence']} r={r['reach']}  {r['note'][:70]}")
        print(f"words={words} penalty={penalty:.2f} median_net={median} add_bar={median - 1}")
        print(f"SCORE {total:.2f}")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
