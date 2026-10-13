# Privacy and Data Handling

## Purpose and Scope

`patra` is a utility library intended to normalize postal locality information. Its scope is strictly confined to postal and geographic address components needed for normalization. Personal identity information and sensitive government identifiers are outside its intended input scope.

## What Patra Processes

`patra` is designed to process only postal normalization inputs. Specifically, the intended input fields are:

* **Locality**: A locality string representing an area, neighborhood, or postal locality name (such as `'andheri west'`).
* **State**: A state name or state input code (such as `'MH'` or `'Maharashtra'`).
* **Pincode**: A six-digit Indian postal PIN code (such as `'400053'`).

These fields are treated solely as normalization inputs (for whitespace trimming, state alias resolution, pincode verification, and title casing) rather than identity or personal profile attributes.

## What Patra Does Not Process

`patra` is not intended to process personal identity documents or government identifiers, including:

* **Aadhaar numbers**
* **Permanent Account Number (PAN) identifiers**
* **Goods and Services Tax Identification Number (GSTIN) identifiers**

These identifiers are not required for postal locality normalization. Users and callers should not pass such identifiers into `patra`, and contributors must not submit them as normalization inputs.

Please note: stating that `patra` does not process personal identifiers defines the intended input scope of the library; it does not constitute an unverified technical guarantee regarding underlying system storage, network transmission, or environment-level retention.

## What we reject

Under our input policy, inputs that resemble sensitive government identifiers are considered unsupported and must be rejected or stripped before submission:

* **Aadhaar-like inputs**: Any 12-digit number or numeric sequence resembling an Aadhaar number.
* **PAN-like inputs**: Any alphanumeric string or input resembling a PAN number (such as a 10-character alphanumeric identifier).

Such values fall outside the supported input scope of postal locality normalization and should be removed or rejected prior to passing data to the library.

## Advisory Policy and Runtime Enforcement

The input rejection policy outlined above is currently **advisory**:

* `patra` **does not yet enforce** this rejection rule at runtime.
* The library does not currently inspect, filter, redact, or automatically reject inputs containing sensitive identifiers in software.
* A documented policy is not an active technical security control. Integrators and callers are responsible for sanitizing and validating inputs prior to passing them to `patra`.

## Safe Contribution and Testing Practices

Contributors to `patra` must follow these privacy practices across all contributions:

* **Do not use real addresses**: Do not include real residential addresses, personal street addresses, or private location details in tests, fixtures, documentation examples, issues, or pull requests.
* **Do not use real personal identifiers**: Never include real or realistic Aadhaar numbers, PAN identifiers, GSTINs, phone numbers, or individual names anywhere in the repository or commit history.
* **Use synthetic placeholders**: When writing tests, examples, or documentation, always use clearly synthetic, non-sensitive placeholders and public locality references (e.g., standard area names and public pincodes).
