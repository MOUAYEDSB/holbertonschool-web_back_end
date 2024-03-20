import redis
import uuid
from typing import Union, Callable
from functools import wraps

class Cache:
    def __init__(self):
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float, None]:
        """Retrieve and optionally convert data from Redis by key."""
        value = self._redis.get(name=key)
        if value is not None and fn:
            return fn(value)
        return value

    def count_calls(method: Callable) -> Callable:
        """A decorator that counts how many times a method is called."""
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            count_key = f"{key}:count"
            self._redis.incr(count_key)
            return method(self, *args, **kwargs)
        return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a random key."""
        key = str(uuid.uuid4())
        self._redis.set(name=key, value=data)
        return key
    