#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    for i in str(number):
        last = i
    print("{}".format(last), end = "")
    return last
