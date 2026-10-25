# SPIFFE standard overview (SPIFFE ID, SVID, Workload API)

URL: https://raw.githubusercontent.com/spiffe/spiffe/main/standards/SPIFFE.md
Type: standard
Read in session: 0004

Summary: SPIFFE = URI identity (SPIFFE ID) for workload; SVID = signed doc carrying ID (X.509, JWT, WIT); Workload API = local endpoint, no auth handshake from workload, issues SVIDs without static secrets. Page silent on agents and credential lifetime; agent fit is inference.

Quotes:
- "A SPIFFE ID is a structured string (represented as a URI)" — SPIFFE.md, section 2
- "It is the functional equivalent of a passport - a document which is presented that carries the identity of the presenter." — SPIFFE.md, section 3, on SVID
- "The SPIFFE Workload API is the method through which workloads, or compute processes, obtain their SVID(s)." — SPIFFE.md, section 4
