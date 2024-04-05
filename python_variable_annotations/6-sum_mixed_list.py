#!/usr/bin/env python3
''' Description: Type-annotated function sum_list
    which takes a list input_list of floats and integers as argument
    and returns their sum as a float.
    Arguments: mxd_lst: list
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns sum of all elements in list'''
    return sum(mxd_lst)
