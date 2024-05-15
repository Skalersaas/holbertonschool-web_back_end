#!/usr/bin/env python3
""" Exercise
"""
import redis
from uuid import uuid4
from typing import Union


class Cache():
    """Cache class"""
    def __init__(self):
        """Initializing"""
        _redis = redis.Redis()
        _redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storing"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
