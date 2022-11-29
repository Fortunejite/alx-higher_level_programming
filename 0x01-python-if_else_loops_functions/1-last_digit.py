#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = 0
for i in str(number):
    last = i
if last > '5':
    print("Last digit of", number, "is", int(last), "and is greater than 5")
elif last == '0':
    print("Last digit of", number, "is", int(last), "and is 0")
elif last < '6' and last != '0':
    print("Last digit of", number, "is", int(last), "and is less than 6 and not 0")
