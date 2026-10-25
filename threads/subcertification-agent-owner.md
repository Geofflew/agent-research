# Who signs the SOX 302 sub-certification for an area an agent prepared?

Status: live
Opened: session 0006B
Yield: 6.66 (0007A C33 +0.86); 0009C C33 +0.68
Graduated: C35 (0006B), merged into C33 (0006B)
Touches: C35, C12, C26, C30
Sources: [cert-17cfr-240-13a-14], [cert-item-601b31-certification-wording], [cert-sec-release-33-8124-fr], [cert-society-corpgov-subcert-benchmark-2018], [cert-ey-society-subcert-survey-2026], [cert-cci-ai-writes-number-reasonable-basis]

What we know so far: 302 certification is personal and non-delegable (13a-14), rests on information made known by others (Item 601(b)(31)); sub-certification is voluntary practice, 11-20 signers most common, 19% 50+ (Society 2018), nearly all quarterly (EY/Society 2026). No source addresses agents as sub-certifiers; C35 infers an agent-owner sub-certification.

What it would take to strengthen: a passage stating what a sub-certifier attests to (judge flagged it unsourced); an SEC comment letter or law-firm memo on certifying officers and AI-prepared amounts; a named authority whose view C35 disagrees with (tension 0).

Open sub-questions:
- Do companies drop sub-certification for agent areas or reassign it?
- Does the agent owner become the AS 2201 control performer of C30?

0007A challenger (C33 kept 8->9, m1->2): sub-certification requests go to process or control owners in departments before officers sign (Highbond help docs, vendor) [subcert2-highbond-automating-302-certification] -> signer = control owner, so agent's owner signs. 57% of companies automated the sub-cert process, 26% hybrid (TCC on 2026 EY/Society survey) [subcert2-tcc-subcerts-common-variation]. Still missing: a primary naming IT/system/automation owners as sub-certifiers.

0008C iter 96 (builder C33, reverted 9->8): SEC charges sub-certifiers for their own signatures [subcert2-sec-wells-fargo-tolstedt-subcerts]; SEC 33-8124 recommends a disclosure committee but has no sub-certification text [subcert2-sec-33-8124-disclosure-committee]; AAR/Sharma order (PDF, not entered) also charges a sub-certifier. Still no primary tying sign-off to who performed the work or owns an automated process. Note: sec.gov and pcaobus.org 403 the scorer UA; use r.jina.ai.

0009C iter 106 (builder C33 kept 7->8, e1->2, +65 words): COSO Feb 2026 GenAI guidance, Principle 3: each GenAI tool needs a named owner with authority and accountability; reliance needs documented prompt, configuration, model version [owner-coso-genai-internal-control-2026] (standard, jina mirror of coso.org PDF). Still inferred: that the named owner signs the 302 sub-certification (COSO does not mention SOX 302). Also new: [owner-sec-33-8810-selfassessment-monitoring] operator self-assessment gives less evidence (counter for owner certifying own agent). COSO also has threshold-change multi-party approval + post-change sampling (C22/C26) and redeployment side-by-side test vs prior model version with control-owner sign-off (C38) - unused.
0009C iter 124 (designer experience C33 reverted 9->8, +28 words): sub-certifier lists the share of the agent's lines a reviewer signed and its error rate from sampling, COSO's metrics ('Percentage of decisions with reviewer sign-off', 'Hallucination rate from sampling') [owner-coso-genai-internal-control-2026]. Not a new step (it names what the certifier lists), so the fall is fair.
