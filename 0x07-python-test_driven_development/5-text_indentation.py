#!/usr/bin/python3
"""
Module 5-text_indentation
Gives a text the right indemt it needs
"""
def text_indentation(text):
    """
    Function defined earlier in the Module
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        word = text.split()
        idx = 0
        for i in word:
            if idx == len(word) - 1:
                print(i, end="")
            elif i[-1] == '.' or i[-1] == ':' or i[-1] == '?':
                print(i, end="")
                print()
                print()
                idx += 1
            else:
                print(i, end=" ")
                idx += 1
                
