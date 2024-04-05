#!/usr/bin/env python3
''' Description: Type-annotated function safe_first_element
    that takes a list lst as argument
    and Checks if list exist, if yes returns first element.
    Arguments: lst: Sequence[Any]
'''

from typing import Optional, Sequence, Any


def __safe_first_element__(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it exists, otherwise returns None.
    
    Args:
        lst (list): The input list.
    
    Returns:
        Optional[Any]: The first element of the list or None if the list is empty.
    """    
    if lst:
        return lst[0]
    else:
        return None
    
