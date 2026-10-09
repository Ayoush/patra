# Normalization pipeline

The `patra.pipeline.normalize()` function applies these steps in order:

1. **Trim** — strip leading and trailing whitespace from the entire input.
2. **Alias** — replace known locality and state aliases with canonical forms (e.g. "Bombay" → "Mumbai", "UK" → "Uttarakhand").
3. **Pincode** — extract and validate the 6-digit PIN from the end of the string.
4. **Casing** — title-case the locality token.

**Example:**

```
Input:  "  BOMBAY 400001  "
Step 1: "BOMBAY 400001"
Step 2: "MUMBAI 400001"  (alias applied)
Step 3: locality="MUMBAI", pincode="400001"
Step 4: locality="Mumbai"
Output: {"locality": "Mumbai", "pincode": "400001", "state": "Maharashtra"}
```

See `src/patra/pipeline.py` for the implementation.
