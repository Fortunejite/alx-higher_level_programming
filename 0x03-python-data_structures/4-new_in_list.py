#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    for i in my_list:
        new.append(i)
    new[idx] = element
    return new
