#!/usr/bin/env python3
"""The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Returns average time'''
    start = time.time()
    for _ in range(4):
        await asyncio.gather(async_comprehension())
    return (time.time() - start) / 4
