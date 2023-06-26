#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if (isinstance(i, int) or
                    (isinstance(i, str) and i.isdigit())) and count < x:
                print("{:d}".format(int(i)), end="")
                count += 1
        print()
        return count
    except (ValueError, TypeError, IndexError):
        pass
