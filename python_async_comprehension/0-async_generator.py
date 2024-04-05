'''
Description: contains function that
yields random numbers once in a second
'''
import asyncio
import random


async def async_generator():
    '''yields random numbers once in a second'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
