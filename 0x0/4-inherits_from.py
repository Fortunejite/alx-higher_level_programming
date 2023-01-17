#!/usr/bin/python3
"""Checks if an onject is an instance of a class."""

def inherits_from(obj, a_class):
    """Returns true if its an instance, otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
