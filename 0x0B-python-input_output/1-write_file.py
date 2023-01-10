#!/usr/bin/python3
"""Morule they reads a given file"""


def write_file(filename="", text=""):
    """prints the content of filename to stdoit"""
    with open(filename, 'w', encoding='utf-8') as file_:
        return file_.write(text)
