#!/usr/bin/env python3
'''
Description: contains function that
yields random numbers once in a second
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''yields random numbers once in a second'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
