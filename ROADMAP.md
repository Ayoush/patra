# patra — 12-week roadmap (Oct–Dec 2026)

## M1 — Foundation (wk 1–2, Oct 6–19)

**Goal:** Beginner track open. CI green. Alias lookup and pincode extraction work.

- [x] Repository setup, CI, devcontainer
- [ ] docs/pipeline.md — normalization order
- [ ] docs/states.md — state alias intro
- [ ] docs/privacy.md — no personal data
- [ ] Bombay → Maharashtra test
- [ ] Pincode extracted from end-of-line test
- [ ] Extra whitespace collapsed test
- [ ] Unknown state left unchanged test

---

## M2 — Core product works end-to-end (wk 3–6, Oct 20 – Nov 16)

**Goal:** `patra norm` works on stdin. Indore aliases added. Devanagari support.

- [ ] patra norm CLI command (Typer, stdin, JSON out)
- [ ] Indore locality aliases (spec/aliases/madhya-pradesh.csv)
- [ ] Devanagari state label मध्य प्रदेश → Madhya Pradesh
- [ ] PIN prefix to region lookup
- [ ] JSONL batch mode (10 in, 10 out)
- [ ] Golden file round-trip test

---

## M3 — Bugs and advanced features (wk 7–10, Nov 17 – Dec 14)

**Goal:** All known bugs fixed. 50+ locality aliases in the catalog.

- [ ] Fix alias match case-sensitive
- [ ] Fix pincode regex eating 10-digit mobile
- [ ] Fix CSV loader dropping quoted commas
- [ ] Fix CLI Unicode crash on Windows
- [ ] Fix region map missing prefix 46
- [ ] 50+ rows across 5 states

---

## M4 — Polish and v1.0 (wk 11–12, Dec 15–28)

**Goal:** 200+ aliases. Public v1.0 release.

- [ ] Full docs review
- [ ] registry/gaps.csv has 0 open rows for M1–M3 scope
- [ ] CHANGELOG.md
- [ ] v1.0 release
