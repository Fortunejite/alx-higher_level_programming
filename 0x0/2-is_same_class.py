#!/usr/bin/python3
"""Checks if an onject is an instance of a class."""

def is_same_class(obj, a_class):
    """Returns true if its an instance, otherwise False."""
    if type(obj) == a_class:
        return True
    else:
        return False
