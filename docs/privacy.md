# Privacy

Patra processes locality names, state names, and six-digit pincodes to
normalize postal address data. It does not process personal identifiers such
as Aadhaar, PAN, or GSTIN.

## Inputs to reject

Do not submit or use inputs that contain values resembling an Aadhaar number
(12 digits), PAN, or GSTIN. This guidance is advisory: Patra does not currently
detect or reject these values automatically. Contributors should use synthetic
data and avoid real addresses in tests and examples.
