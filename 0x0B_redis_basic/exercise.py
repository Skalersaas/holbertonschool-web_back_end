#!/usr/bin/env python3
""" Exercise
"""
import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator"""
    key = method.__qualname__
    @wraps(method)

    def wrapper(self, *args, **kwargs):
        '''wrapper'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Call history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''wrapper'''
        input = str(args)
        output = str(method(self, *args,**kwargs)) 
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper

def replay(method: Callable):
    r = redis.Redis()
    qn = method.__qualname__
    calls = r.get(qn)
    try:
        calls = calls.decode('utf-8')
    except Exception:
        calls = 0
    print(qn, f"was called {calls} times")
    inputs = r.lrange(qn+":inputs", 0, -1)
    outputs = r.lrange(qn+":outputs", 0, -1)
    
    for i in range(len(inputs)):
        print(f"{qn}(*{inputs[i].decode('utf-8')}) -> {outputs[i].decode('utf-8')}")

class Cache():
    """Cache class"""
    def __init__(self):
        """Initializing"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Storing"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get"""
        val = self._redis.get(key)
        if fn:
            return fn(val)

        return val

    def get_str(self, key: str) -> str:
        """Get string"""
        return self._redis.get(key).decode('utf-8')

    def get_int(self, key: str) -> int:
        """Get int"""
        val = self._redis.get(key)
        try:
            val = int(val.decode('utf-8'))
        except Exception:
            val = 0
        return val
