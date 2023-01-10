#!/usr/bin/python3
"""Morule they reads a given file"""


def append_write(filename="", text=""):
    """prints the content of filename to stdoit"""
    with open(filename, 'a+', encoding='utf-8') as file_:
        return file_.write(text)
