#!/usr/bin/python3
"""Prints the sorted lists of a class."""

class MyList(list):
    """Just printe the sorted types."""
    def print_sorted(self):
        """prints in accendimg order."""
        print(sorted(self))
