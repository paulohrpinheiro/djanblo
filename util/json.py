"""
Json converter.
"""

import json


def to_json(from_string):
    """Convert string to json."""
    # Only python >= 3.6 accept str & bytes in json.loads
    return json.loads(str(from_string, 'utf-8'))
