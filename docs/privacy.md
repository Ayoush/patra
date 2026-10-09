# Privacy policy for fixtures

## What patra stores

patra's fixtures contain locality names and PIN codes only. No street addresses, no person names, no phone numbers, no email addresses.

## Rejection rule

A fixture row is rejected (and the PR closed) if it contains:
- Any string that could be a person's name
- Any phone number or mobile number
- Any street-level address (house number, flat number, road name)
- Any PAN, Aadhaar, or other government identifier

If you are unsure whether a string is personal data, leave it out.

## Why this matters

This is an open-source repository visible to everyone. Personal data in source code is a privacy violation that is difficult to fully remediate (git history, forks, caches).
