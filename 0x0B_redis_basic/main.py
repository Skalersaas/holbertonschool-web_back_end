"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()
cache.store(2)

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
