from .._json import error_envelope

NO_TOKEN = error_envelope(
    "not_configured",
    "No Cove Data Protection credentials. Send the X-CoveDataProtection-Partner, "
    "X-CoveDataProtection-Username, and X-CoveDataProtection-Password headers.",
    False,
)
