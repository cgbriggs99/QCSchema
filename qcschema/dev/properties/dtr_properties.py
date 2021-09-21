
import copy
import dev_schema

dtr_properties = {
    "Da": {
        "type": "array",
        "description": "The one-particle density matrix",
        "items": {
            "type": "number"
            }
        }
    "T2": {
        "type": "array",
        "description": "The T2 amplitudes",
        "items": {
            "type": "number"
            }
        }
    }

