#!/usr/bin/env python3
'''
Description: contains function that
yields random numbers once in a second
'''
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension () -> List[float]:
    '''yields random numbers once in a second'''
    return [i async for i in async_generator()]