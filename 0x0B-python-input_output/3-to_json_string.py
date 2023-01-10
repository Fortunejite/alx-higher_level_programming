#!/usr/bin/python3
"""Returns JSON represent of an onjecy"""


def to_json_string(my_obj):
    """Cinverts object to string"""
    import json
    return json.dumps(my_obj)
