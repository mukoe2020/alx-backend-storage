#!/usr/bin/env python3
"""
create a Cache class that will implement a simple cache using Redis
"""

from crypt import Method
import redis
import uuid
from typing import Union
from functools import wraps


class Cache:
    """
    a class that stores redis instance as a private variable
    """
    def __init__(self):
        """
        constructor for Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store the input data in redis using a random key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    
    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        """
        convert data back to the desired format
        """
        data = self._redis.get(key)
        if self._redis.exists(key):
            data = self._redis.get(key)
            if fn:
                return fn(data)
            else:
                return data
        else:
            return None

    def get_str(data: bytes) -> str:
        """
        convert bytes to string
        """
        return data.decode('utf-8')

    def get_int(data: bytes) -> int:
        """
        convert bytes to int
        """
        return int(data.decode('utf-8'))

    def count_calls(fn: callable) -> callable:
        """
        return function that increments the count for that key
        method is called and returns value returned by the original method.
        """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return _Method(self, *args, **kwargs)
    return wrapper
