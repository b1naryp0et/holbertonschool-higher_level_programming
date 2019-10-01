#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for i in range(x):
        y = y + 1
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            y = y - 1
    print()
    return y
