#!/usr/bin/python3
"""Getting mir complex with JSON"""


import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    args = load('add_item.json')
except:
    args = []
for i in sys.argv:
    args.append(i)
args = args[1:]
try:
    save(args, 'add_item.json')
except:
    pass
