#!/usr/bin/python3
from operator import ne


def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in new_dictionary.items():
        new_dictionary[key] *= 2
    return (new_dictionary)
