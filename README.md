# Privacy

Patra normalizes Indian postal addresses offline. This page explains what data Patra processes, what it does not process, and how contributors should handle test data.

## What Patra processes

Patra processes only these three inputs:

- **Locality string**: an area, neighbourhood, or town name, in Latin or Devanagari script, for example `Koramangala` or `अंधेरी`. Patra normalizes its casing and, for Devanagari input, maps it to a Latin label using bundled data.
- **State name**: for example `Karnataka`, or an alias such as `KA`. Patra normalizes aliases to a standard state name.
- **Pincode**: a 6-digit Indian postal code, for example `560034`. Patra checks and normalizes its format only. It does not check whether the pincode exists or belongs to the given state or locality.

None of these identifies a person. Each one describes a place shared by many people.

Patra works offline. Normalization uses data bundled with the project, and addresses are not sent to any external geocoding or postal service.

## What Patra does not process

Patra does not extract, validate, or process personal or business identifiers, including:

- **Aadhaar numbers**
- **PAN** (Permanent Account Number)
- **GSTIN** (Goods and Services Tax Identification Number)

These fall outside the scope of postal address normalization. Do not pass them to Patra. If you are working with full customer records, extract the locality, state, and pincode first, and pass only those.

## What we reject

Inputs that contain what looks like an **Aadhaar number** (a 12-digit number, with or without spaces or hyphens, such as `1234 5678 9012`) should be treated as rejected and must not be passed to Patra.

### This policy is advisory

Patra does **not** enforce this rejection yet. Patra validates the format of 6-digit pincodes, but it will not currently detect or block a 12-digit number elsewhere in the input. Until enforcement is added, it is up to you, as a user or contributor, to keep these values out.

## Guidance for contributors

- **Do not test with real addresses.** Use made-up locality strings, or public places such as post offices or landmarks, together with their real pincodes.
- **Never use real identifiers in tests, fixtures, examples, or issues.** This includes Aadhaar, PAN, and GSTIN numbers. If a test needs a value that looks like an Aadhaar number, use an obviously fake one such as `0000 0000 0000`.
- **Do not paste real user data into bug reports.** Reduce it to the locality, state, and pincode needed to reproduce the problem.

## Reporting a privacy issue

If you find that Patra handles personal data in a way this page does not describe, please open an issue on the repository.
