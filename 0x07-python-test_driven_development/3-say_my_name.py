#!/usr/bin/python3
"""
Moudle 3-say_my_name
It prints the first and last name entered
Also it do some test for perfect code
"""
def say_my_name(first_name, last_name=""):
    """
    The moudle that dies everything
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
