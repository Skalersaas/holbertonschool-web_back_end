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
        val = self._redis.get(key)
        if fn:
            return fn(val)

        return val

    def get_str(self, key: str) -> str:
        """Get string"""
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> str:
        """Get int"""
        val = self._redis.get(key)
        try:
            return int(val)
        except Exception:
            return 0
