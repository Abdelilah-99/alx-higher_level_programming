#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    import sys
    for i in range(len(sys.argv)):
        if i > 3:
            print("Usage: ./100-my_calculator.py <a> <operator> <b>")
            exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], add(a, b)))
    elif sys.argv[2] == "-":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], sub(a, b)))
    elif sys.argv[2] == "*":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], mul(a, b)))
    elif sys.argv[2] == "/":
        print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
