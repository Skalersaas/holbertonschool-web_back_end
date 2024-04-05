#!/usr/bin/env python3
''' Description: Type-annotated function safe_first_element
    that takes a list lst as argument
    and Checks if list exist, if yes returns first element.
    Arguments: lst: Sequence[Any]
'''

from typing import Optional, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    '''Checks if list exist, if yes returns first element'''
    if lst:
        return lst[0]
    else:
        return None