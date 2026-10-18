# Patra

Patra is a project for offline normalization of Indian postal addresses,
focusing on state aliases, pincode formatting, locality casing, and
data-driven Devanagari-to-Latin locality labels.

### What Patra Does NOT Do

- **Geocoding and Geotagging:** Patra does not convert postal addresses
  into geographic coordinates or assign location tags. These operations
  require external geographic reference data or geocoding services.

- **Postal Address Verification:** Patra does not verify whether an
  address physically exists or can receive mail. Such verification
  requires authoritative postal databases or external services.

- **Aadhaar/PAN Processing:** Patra does not extract, validate, or
  process Aadhaar, PAN, or other government-issued identity identifiers.
  These fall outside the scope of postal address normalization.

- **English-to-Hindi Transliteration:** Patra does not convert English
  address text into Devanagari script. Its functionality is limited to
  data-driven Devanagari-to-Latin locality labels.

- **Pincode-to-State Verification:** Patra validates pincode formatting
  but does not verify whether a pincode belongs to a specific state
  or locality. This requires a reliable, up-to-date postal dataset.

#### File Description
- [State and UT aliases](docs/states.md): historical names and why they changed