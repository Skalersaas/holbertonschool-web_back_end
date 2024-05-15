#!/usr/bin/env python3
""" Exercise
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable


class Cache():
    """Cache class"""
    def __init__(self):
        """Initializing"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storing"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """Get"""
        if fn:
            return fn(key)

        return self._redis.get(key)
