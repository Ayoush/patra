# Pipeline Worked Example

**Starting Input:**
* Locality: `' andheri west '`
* State: `'MH'`
* Pincode: `'400053'`

**Step 1: Whitespace**
* Removes the extra spaces at the beginning and end.
* Current value: `'andheri west'`

**Step 2: Alias**
* Checks if there is another official name for this place.
* Current value: `'andheri west'`

**Step 3: Pincode**
* Checks the postal code to make sure it matches the area.
* Current value: `'andheri west'`

**Step 4: Casing**
* Fixes the big and small letters.
* Final output: `'Andheri West'`

**What does `state_was_alias` mean?**
This is a label that tells us if the state we started with was a short nickname (like 'MH') instead of its full official name (like 'Maharashtra').

