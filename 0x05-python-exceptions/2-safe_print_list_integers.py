#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end='')
            elements_printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return (elements_printed)