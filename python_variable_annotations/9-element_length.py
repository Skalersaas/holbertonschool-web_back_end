#!/usr/bin/env python3
''' Description: Type-annotated function element_length
    that takes a list lst as argument
    and returns a List of tuples with all elements and their lengths.
    Arguments: lst: Iterable[Sequence]
'''

from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a List of tuples with all elements and their lengths'''
    return [(i, len(i)) for i in lst]