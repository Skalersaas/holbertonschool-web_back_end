#!/usr/bin/env python3
''' Description: Type-annotated function make_multiplier
    that takes a float multiplier as argument
    and returns a function that multiplies a float by multiplier.
    Arguments: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Returns sum of all elements in list'''
    def multiply_by(m: float)-> float:
        return multiplier * m
    return multiply_by
