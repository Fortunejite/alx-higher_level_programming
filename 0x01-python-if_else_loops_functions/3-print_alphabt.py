#!/usr/bin/python3
for lett in range(ord('a'), ord('z')+1):
    if lett == ord('q') or lett == ord('e'):
        continue
    print("{:c}".format(lett), end="")
