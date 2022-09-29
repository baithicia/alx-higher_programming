#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sub_dictionary = a_dictionary.copy()
    for key, value in sorted(sub_dictionary.items(), key = lambda x: [0]):
        print("{} : {}". format(key, value))
    return sub_dictionary

