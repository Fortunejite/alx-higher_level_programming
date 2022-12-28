#!/usr/bin/python3
"""
Module which prints square
Takes in the size of squqre
"""
def print_square(size):
    """
    Described above
    """
    msg = "size must be an integer"
    if not isinstance(size, int):
        raise TypeError(msg)
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
