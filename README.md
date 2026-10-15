# patra

Patra is a project for offline normalization of Indian postal addresses,
focusing on state aliases, pincode formatting, locality casing, and
data-driven Devanagari-to-Latin locality labels.

### What patra does NOT do

- **Geocoding and Geotagging**
  - Patra does not convert postal addresses into geographic coordinates
    (latitude and longitude) or assign geographic tags to locations.
  - These operations require geographic reference data or integration
    with an external geocoding service, which may involve a paid API.
  - Such integrations fall outside Patra's offline normalization scope.

- **Postal Address Verification**
  - Patra does not verify whether a postal address physically exists
    or can successfully receive mail.
  - Reliable address verification requires access to authoritative
    postal databases or external verification services.
  - Patra focuses on normalizing address data rather than confirming
    real-world address validity.

- **Aadhaar/PAN Processing**
  - Patra does not extract, validate, or process Aadhaar numbers,
    PAN numbers, or other government-issued identity identifiers.
  - Processing such identifiers falls outside the scope of postal
    address normalization and may involve sensitive personal information.

- **English-to-Hindi Transliteration**
  - Patra does not automatically convert English-script address text
    into Hindi (Devanagari) script.
  - This functionality requires additional transliteration rules,
    language-processing tools, or dedicated language models.
  - Patra's documented approach instead focuses on data-driven
    Devanagari-to-Latin locality labels.

- **Pincode-to-State Verification**
  - Patra does not provide authoritative verification that a given
    pincode belongs to a particular Indian state.
  - Checking a pincode's format does not guarantee that the pincode
    corresponds to the supplied state or locality.
  - Such verification requires an accurate and regularly maintained
    postal reference dataset.
