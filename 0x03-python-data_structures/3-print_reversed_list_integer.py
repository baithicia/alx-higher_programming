#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for int in my_list:
            return int
    else:
        next(iter([]))
        
    my_list.reverse()
    print(":d".format(my_list))



