#!/usr/bin/env python3
''' Description: Type-annotated function floor
    which takes a float n
    as argument and returns the floor of the float.
'''


import math

def floor(n: float) ->int:
    '''Returns sum of two numbers with floating point'''
    return int(math.floor(n))
