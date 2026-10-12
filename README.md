# patra

> Offline normalizer for Indian postal addresses: state aliases, pincode shape, locality casing, and Devanagari-to-Latin locality labels.

**Offline · No personal data · Locality + PIN only · Apache-2.0**

[![CI](https://github.com/Ayoush/patra/actions/workflows/ci.yml/badge.svg)](https://github.com/Ayoush/patra/actions/workflows/ci.yml)

---

## Run it in 5 minutes

**Prerequisites:** Python 3.12+

```bash
git clone https://github.com/Ayoush/patra.git
cd patra
make dev
```

`make dev` creates a virtual environment, installs dependencies, runs the linter, and runs the full test suite. Everything runs offline.

**In Codespaces or a devcontainer:** click **Code → Codespaces → Create codespace on main** or **Reopen in Container** in VS Code.

---

## What this is

Indian addresses are spelled in dozens of ways: "Bombay" vs "Mumbai", "UK" vs "Uttarakhand", "मुंबई" vs "Mumbai". This repo normalizes them to a canonical form using a table of known aliases.

Each unit of work is one locality or alias row in `spec/aliases/`. A contributor adds a row; a test proves the normalization. The table never closes.

---

## Project layout

```
src/patra/
  alias.py       # Alias lookup (state + locality)
  pincode.py     # Extract and validate pincode
  whitespace.py  # Collapse and clean whitespace
  pipeline.py    # Normalization pipeline (trim → alias → pincode → casing)
  load.py        # CSV loader for alias tables
  cli.py         # patra norm command
  pin_prefix.py  # PIN prefix → region lookup
spec/aliases/    # One CSV per state
fixtures/
  raw/           # Input addresses
  golden/        # Expected normalized output (JSONL)
registry/
  gaps.csv       # AI planner reads this
docs/
  pipeline.md    # Normalization order
  states.md      # State alias table intro
  privacy.md     # No personal names in fixtures
```

---

## Quick example

```bash
echo '{"raw": "Bombay 400001"}' | python -m patra norm
# {"state": "Maharashtra", "locality": "Mumbai", "pincode": "400001", "raw": "Bombay 400001"}
```

---

## Stack

| Layer | Tool |
|-------|------|
| Language | Python 3.12 |
| Testing | pytest |
| Lint / Format | ruff |
| Type checking | mypy |
| CLI | Typer |

---

## Contributing

New here? Start with a [`good first issue`](../../issues?q=label%3A%22good+first+issue%22). See [CONTRIBUTING.md](CONTRIBUTING.md).
