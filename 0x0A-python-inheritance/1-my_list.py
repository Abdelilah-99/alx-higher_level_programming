#!/usr/bin/python3
"""print list"""


class MyList(list):
    """in sorted"""
    def print_sorted(self):
        print(sorted(self))
