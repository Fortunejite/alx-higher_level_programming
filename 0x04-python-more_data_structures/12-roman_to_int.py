#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    elif roman_string == "":
        return 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    last = ''
    result = 0
    for i in roman_string:
        if i not in value.keys():
            return 0
        elif last == '':
            last = i
            result += value[i]
        elif value[i] > value[last]:
            result = value[i] - result
            last = i
        else:
            result += value[i]
            last = i
    return result
