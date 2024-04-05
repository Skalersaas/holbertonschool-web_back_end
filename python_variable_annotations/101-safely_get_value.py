#!/usr/bin/env python3
"""This module contains a type annotated function that uses TypeVar"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar("T")


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Returns a value from a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default