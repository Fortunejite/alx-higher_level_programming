#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    count = 0
    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            idx += 1
            count += 1
        except (TypeError, ValueError):
            idx += 1
            continue
    print()
    return count
