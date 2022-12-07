#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    num = 0
    for i in a_dictionary:
        if a_dictionary[i] > num:
            num = a_dictionary[i]
            us = i
    return us
