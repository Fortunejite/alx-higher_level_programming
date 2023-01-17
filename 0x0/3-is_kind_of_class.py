#!/usr/bin/python3
"""Checks if an onject is an instance of a class."""

def is_kind_of_class(obj, a_class):
    """Returns true if its an instance, otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
