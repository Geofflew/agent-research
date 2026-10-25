#!/usr/bin/env python3
"""Score scenarios/*.md with the scenario rubric. No source gate: scenarios may go beyond the
sources. score = Σ_scenarios (sum of 7 dims) − words/300. Judge: fixed model, median of 3,
cached by text. usage: python3 eval/score_scenarios.py [--json] [--focus slug]"""
import argparse, shutil
from pathlib import Path
import hashlib, json, os, re, statistics, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "eval", ".cache")
JUDGE_MODEL = os.environ.get("JUDGE_MODEL", "sonnet")
DIMS = ["coherence", "anchoring", "clocks", "mechanism", "reach", "consequence", "surprise"]
WORDS_PER_POINT = 300
os.makedirs(CACHE, exist_ok=True)
def read(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read()


def claim_titles():
    t = read(os.path.join(ROOT, "thesis.md"))
    out = []
    for m in re.finditer(r"^## (C\d+)\.\s*(.+?)\n(.*?)(?=^## C\d+\.|\Z)", t, re.M | re.S):
        if not re.search(r"^Confidence:\s*retired", m.group(3), re.M):
            out.append(f"{m.group(1)}. {m.group(2).strip()}")
    return "\n".join(out)


def judge(text, question, rubric, titles, samples):
    key = "scen-" + hashlib.sha1((JUDGE_MODEL + question + text + rubric + titles + str(samples)).encode()).hexdigest()
    p = os.path.join(CACHE, key)
    if os.path.exists(p):
        return json.loads(read(p))
    prompt = (rubric + "\n\nRESEARCH QUESTION:\n" + question + "\n\nDEFENDED CLAIMS (titles):\n" + titles
              + "\n\nSCENARIO:\n" + text + "\n\nJSON:")
    results = []
    for _ in range(samples):
        try:
            r = subprocess.run(["claude", "-p", "--model", JUDGE_MODEL, "--output-format", "json"],
                               input=prompt, capture_output=True, text=True, timeout=180)
            if r.returncode:
                raise RuntimeError("Judge CLI exited with an error; check CLI authentication and model access")
            txt = json.loads(r.stdout).get("result", "")
            results.append(json.loads(re.search(r"\{.*\}", txt, re.S).group(0)))
        except Exception as e:  # noqa
            results.append({"err": str(e)[:100]})
    good = [r for r in results if all(type(r.get(d)) is int and 0 <= r[d] <= 2 for d in DIMS)]
    if len(good) < samples // 2 + 1:
        raise RuntimeError("Judge returned too few valid samples; no score was cached")
    out = {d: statistics.median(int(r[d]) for r in good) for d in DIMS} | {"note": good[0].get("note", "")}
    out["samples"] = results
    with open(p, "w") as f:
        json.dump(out, f)
    try:
        import datetime as _dt
        with open(os.path.join(ROOT, "judge-log.tsv"), "a") as f:
            f.write("\t".join([_dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M"), "scenario",
                               json.dumps([{d: r.get(d) for d in DIMS} for r in good])]) + "\n")
    except Exception:
        pass
    return out


def check_local():
    """Validate scenario metadata and anchor existence without a model call."""
    text = read(os.path.join(ROOT, "thesis.md"))
    ids = set(re.findall(r"^## (C\d+)\.", text, re.M))
    count = 0
    errors = []
    for path in sorted(Path(ROOT, "scenarios").glob("*.md")):
        if path.name == "README.md":
            continue
        scenario = path.read_text(encoding="utf-8")
        if re.search(r"^Status:\s*retired", scenario, re.M):
            continue
        count += 1
        if not re.search(r"^Year:\s*20\d{2}", scenario, re.M):
            errors.append(f"{path.name}: missing Year")
        if not re.search(r"^Status:\s*live", scenario, re.M):
            errors.append(f"{path.name}: missing live Status")
        for anchor in re.findall(r"\bC\d+\b", scenario):
            if anchor not in ids:
                errors.append(f"{path.name}: missing claim {anchor}")
    if errors:
        raise RuntimeError("\n".join(errors))
    print(f"Local scenario check passed: {count} live scenarios; claim IDs resolve. No network or model calls.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate local files without network or model calls")
    parser.add_argument("--json", action="store_true", help="Print live evaluation as JSON")
    parser.add_argument("--focus", metavar="ID", help="Use five samples for a selected claim or scenario")
    args = parser.parse_args()
    if args.check:
        check_local()
        return
    if shutil.which("claude") is None:
        parser.error("Live evaluation requires an installed and authenticated Claude CLI; use --check for offline validation")
    question = read(os.path.join(ROOT, "question.md"))
    rubric = read(os.path.join(ROOT, "eval", "scenario-rubric.md"))
    titles = claim_titles()
    focus = sys.argv[sys.argv.index("--focus") + 1] if "--focus" in sys.argv else None
    d = os.path.join(ROOT, "scenarios")
    rows, total, words_all = [], 0.0, 0
    for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        if not fn.endswith(".md") or fn == "README.md":
            continue
        slug = fn[:-3]
        text = read(os.path.join(d, fn))
        if re.search(r"^Status:\s*retired", text, re.M):
            continue
        words = len(text.split()); words_all += words
        j = judge(text, question, rubric, titles, 5 if focus == slug else 3)
        s = sum(j[k] for k in DIMS)
        total += s
        rows.append({"slug": slug, "score": s, "words": words, **{k: j[k] for k in DIMS}, "note": j["note"]})
    penalty = words_all / WORDS_PER_POINT
    total -= penalty
    out = {"score": round(total, 2), "words": words_all, "penalty": round(penalty, 2), "scenarios": rows}
    if "--json" in sys.argv:
        print(json.dumps(out, indent=1))
    else:
        for r in rows:
            print(f"{r['slug']:>34} score={r['score']:>2} " + " ".join(f"{k[:3]}={r[k]}" for k in DIMS) + f"  {r['note'][:60]}")
        print(f"words={words_all} penalty={penalty:.2f}")
        print(f"SCENARIO SCORE {total:.2f}")


if __name__ == "__main__":
    try:
        main()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
