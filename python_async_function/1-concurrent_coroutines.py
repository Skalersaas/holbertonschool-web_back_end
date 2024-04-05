#!/usr/bin/env python3
""" continue at the same time witha sync """
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
