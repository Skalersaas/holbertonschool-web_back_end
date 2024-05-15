#!/usr/bin/env python3
""" Tasks - Redis """
import redis
import requests
from typing import Callable
from functools import wraps


r = redis.Redis()

def counter(method: Callable) -> Callable:
    """Counts"""
    
    @wraps
    def wrapper(url):
        r.incr(f'count:{url}')
        html = r.get(f'cached:{url}')
        if html:
            return html.decode('utf-8')
        
        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@counter
def get_page(url: str) -> str:
    """Get page from url"""
    return requests.get(url).text