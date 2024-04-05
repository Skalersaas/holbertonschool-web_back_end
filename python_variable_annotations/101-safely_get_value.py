#!/usr/bin/env python3
''' Description: Type-annotated function safe_first_element
    that takes a list lst as argument
    and Checks if list exist, if yes returns first element.
    Arguments: lst: Sequence[Any]
'''

from typing import Mapping, Any, Union, TypeVar



T = TypeVar("T")
def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default