#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    idx = 0
    while idx < list_length:
        try:
            ans = my_list_1[idx] / my_list_2[idx]
            idx += 1
        except ZeroDivisionError:
            idx += 1
            ans = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
            ans = 0
            idx += 1
        except IndexError:
            print("out of range")
            ans = 0
            idx += 1
        finally:
            new.append(ans)
    return new
            
