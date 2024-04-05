#!/usr/bin/env python3
'''
Description: contains function that
yields random numbers once in a second
'''
import asyncio
import random
from typing import Generator
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension () -> Generator[float, None, None]:
    '''yields random numbers once in a second'''
    return async_generator()
