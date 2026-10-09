# Contributing to patra

Welcome! patra is part of **Intervues Lab**. This guide explains everything you need.

---

## Quick overview

1. Find an issue, comment `I'll take this` to claim it.
2. Fork → branch → code → tests → PR.
3. Gremlin (AI reviewer) comments. A human mentor approves.
4. Fix feedback, get merged.

---

## Fork and clone

```bash
git clone https://github.com/YOUR-USERNAME/patra.git
cd patra
git remote add upstream https://github.com/Ayoush/patra.git
```

## Set up the environment

```bash
make dev       # creates venv, installs, lints, tests
make test      # tests only
make lint      # ruff only
make typecheck # mypy only
```

## Commit style

Conventional Commits:

```
feat(alias): add Indore locality aliases
fix(pincode): 10-digit mobile not captured as PIN
docs: document normalization order in pipeline.md
test(aliases): Bombay maps to Maharashtra
```

## Adding an alias row

1. Add a row to `spec/aliases/<state>.csv`: columns are `raw`, `normalized`, `state`.
2. Update `registry/gaps.csv` — set `status` to `done`.
3. Add a test in `tests/test_aliases.py`.
4. Run `make test`.

**No personal data in fixtures.** Locality names and pincodes only — no street names, person names, or phone numbers. The PR template asks you to confirm.

## What a good PR looks like

- One alias file or one fix per PR.
- All tests pass locally.
- PR description fills every section of the template.
- Names one alternative you rejected.

## Review flow

1. **Gremlin** posts automated feedback.
2. Fix issues, comment `ready for mentor review`.
3. **Human mentor** approves and merges.

## Registry format

`registry/gaps.csv` columns: `state`, `locality`, `status` (open/done), `owner` (GitHub username or blank).
