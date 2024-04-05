#!/usr/bin/env python3
''' Description: Type-annotated function sum_list
    which takes a list input_list of floats as argument
    and returns their sum as a float.
    Arguments: input_list: list
'''


def sum_list(input_list: list) -> float:
    '''Returns sum of all elements in list'''
    return sum(input_list)