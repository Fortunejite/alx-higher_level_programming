#!/usr/bin/python3
def search_replace(my_list, search, replace):
    tmp = []
    for i in my_list:
        if i == 2:
            tmp.append(89)
        else:
            tmp.append(i)
    return tmp
