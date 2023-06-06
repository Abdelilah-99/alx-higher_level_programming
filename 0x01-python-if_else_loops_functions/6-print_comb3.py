#!/usr/bin/python3
for i in range(10):
    for j in range(i+1, 10):
        print("{}{}".format(i, j), end=", ")
        if i == 7 and j == 9:
            print("89")
            exit(0)
