#!/usr/bin/python3
"""Returns JSON represent of an onjecy"""


def save_to_json_file(my_obj, filename):
    """Cinverts object to string"""
    import json
    json_str = json.dumps(my_obj)
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(json_str)
