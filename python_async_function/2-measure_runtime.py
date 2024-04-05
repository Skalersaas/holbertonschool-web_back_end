#!/usr/bin/env python3
""" function measures wait_n execution time """
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: float) -> float:
    '''to measure time'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.time() - start
    return elapsed_time / n
