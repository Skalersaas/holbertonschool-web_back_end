#!/usr/bin/env python3
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    float time random
    """
    list = []

    for _ in range(n):
        list.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(list):
        list.pop(0)
        list.append(await task)

    return list
