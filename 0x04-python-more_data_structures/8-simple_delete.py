#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionart[key]
        return a_dictionary
    else:
        return None
