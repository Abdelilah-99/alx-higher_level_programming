#!/usr/bin/env python3
def uppercase(str):
    str1 = ""
    for i in str:
        if 97 <= ord(i) <= 122:
            str1 += chr(ord(i) - 32)
        else:
            str1 += i
    print("{}".format(str1))
