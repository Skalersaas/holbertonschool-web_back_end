#!/usr/bin/env python3
''' Description: Asynchronous coroutine that takes in an integer argument
    (max_delay, with a default value of 10) named wait_random
    that waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it.
'''
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    float time random
    """
    list = []

    for _ in range(n):
        list.append(wait_random(max_delay))

    for task in asyncio.as_completed(list):
        list.pop(0)
        list.append(await task)

    return list
