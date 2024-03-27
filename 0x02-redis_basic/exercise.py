#!/usr/bin/env python3
"""
create a Cache class that will implement a simple cache using Redis
"""

import redis
import uuid
from typing import Union


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
        if fn:
            return fn(data)
        return data



