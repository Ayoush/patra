"""State name alias resolution."""

# Maps common abbreviations and misspellings to canonical state names.
# Keys are UPPERCASE for case-insensitive lookup.
STATE_ALIASES: dict[str, str] = {
    # Official abbreviations
    "AP": "Andhra Pradesh",
    "AR": "Arunachal Pradesh",
    "AS": "Assam",
    "BR": "Bihar",
    "CG": "Chhattisgarh",
    "GA": "Goa",
    "GJ": "Gujarat",
    "HR": "Haryana",
    "HP": "Himachal Pradesh",
    "JH": "Jharkhand",
    "KA": "Karnataka",
    "KL": "Kerala",
    "MP": "Madhya Pradesh",
    "MH": "Maharashtra",
    "MN": "Manipur",
    "ML": "Meghalaya",
    "MZ": "Mizoram",
    "NL": "Nagaland",
    "OR": "Odisha",
    "OD": "Odisha",
    "PB": "Punjab",
    "RJ": "Rajasthan",
    "SK": "Sikkim",
    "TN": "Tamil Nadu",
    "TS": "Telangana",
    "TR": "Tripura",
    "UP": "Uttar Pradesh",
    "UK": "Uttarakhand",
    "UA": "Uttarakhand",
    "WB": "West Bengal",
    # Union territories
    "AN": "Andaman and Nicobar Islands",
    "CH": "Chandigarh",
    "DN": "Dadra and Nagar Haveli and Daman and Diu",
    "DD": "Dadra and Nagar Haveli and Daman and Diu",
    "DL": "Delhi",
    "LD": "Lakshadweep",
    "PY": "Puducherry",
    "PO": "Puducherry",
    "LA": "Ladakh",
    # Historical / informal names
    "BOMBAY": "Maharashtra",
    "MADRAS": "Tamil Nadu",
    "CALCUTTA": "West Bengal",
    "ORISSA": "Odisha",
    "PONDICHERRY": "Puducherry",
    "UTTARANCHAL": "Uttarakhand",
    "UTTARPRADESH": "Uttar Pradesh",
    "MADHYAPRADESH": "Madhya Pradesh",
    "J&K": "Jammu & Kashmir",
    "JK": "Jammu & Kashmir",
    "J AND K": "Jammu & Kashmir",
    "JAMMU AND KASHMIR": "Jammu & Kashmir",
}


def resolve_state_alias(name: str) -> str:
    """Return the canonical state name, or the input unchanged if not an alias."""
    return STATE_ALIASES.get(name.strip().upper(), name)
