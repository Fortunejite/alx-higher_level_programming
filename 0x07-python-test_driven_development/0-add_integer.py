#!/usr/bin/python3
"""
Module 0-add_integer
Contains ome method that adds up num
Accepts two integer then converts to int before adding
"""
def add_integer(a, b=98):
    """
    Returns a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
