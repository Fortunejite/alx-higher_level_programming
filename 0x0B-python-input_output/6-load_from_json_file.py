#!/usr/bin/python3
"""Returns JSON represent of an onjecy"""


def load_from_json_file(filename):
    """Cinverts object to string"""
    import json
    
    with open(filename, 'r', encoding='utf-8') as f:
        
        json_str = f.read()
        return json.loads(json_str)
