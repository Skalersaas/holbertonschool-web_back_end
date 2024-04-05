#!/usr/bin/env python3
"""This module contains an annotated function that
returns info about a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element of a sequence or none"""
    if lst:
        return lst[0]
    else:
        return None