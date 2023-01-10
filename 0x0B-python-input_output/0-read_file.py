#!/usr/bin/python3
"""Morule they reads a given file"""


def read_file(filename=""):
    """prints the content of filename to stdoit"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
