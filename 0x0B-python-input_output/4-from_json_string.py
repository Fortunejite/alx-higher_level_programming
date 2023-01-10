#!/usr/bin/python3
"""Returns JSON represent of an onjecy"""


def from_json_string(my_obj):
    """Cinverts object to string"""
    import json
    return json.loads(my_obj)
