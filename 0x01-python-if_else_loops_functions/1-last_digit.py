#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs(number)
last = int(list(str(number))[-1])
last = -last if number < 0 else last
print("last digit of {} is {} and is".format(number, last), end=" ")
if last > 5:
    print("greater than 5")
elif last != 0:
    print("less than 6 and not 0")
else:
    print("0")
