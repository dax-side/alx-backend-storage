#!/usr/bin/env python3
""" defines a class Cache"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ decorator"""
    key = method.__qualname__

    @wraps(method)
    def increment(self, *args, **kwargs):
        """ increment count for the key in count_calls"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return increment


def call_history(method: Callable) -> Callable:
    """ Decorator"""
    @wraps(method)
    def wrapped(self, *args, **kwargs):
        """ store input and output"""
        Input = str(args)
        q_name = method.__qualname__
        self._redis.rpush(q_name + ":inputs", Input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(q_name + ":outputs", output)
        return output
    return wrapped


def replay(fn: Callable):
    """ display history of calls of a function"""
    r = redis.Redis()
    func_name = fn.__qualname__
    count = r.get(func_name)
    try:
        count = int(count.decode('utf-8'))
    except Exception:
        count = 0
    print("{} was called {} times:".format(func_name, count))
    inputs = r.lrange("{}:inputs".format(func_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(func_name), 0, -1)
    for one, two in zip(inputs, outputs):
        try:
            one = o.decode('utf-8')
        except Exception:
            one = ""
        try:
            two = t.decode('utf-8')
        except Exception:
            two = ""
        print("{}(*{},) -> {}".format(func_name, one, two))


class Cache():
    """ stores an instance of the redis client"""
    def __init__(self):
        """ Constructor"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """" generate a random key using uuid"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ extract informtion saved in redis"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """ Automatically parametrize Cache.get
            with the correct conversion function.
        """
        value = self._redis.get(key)
        return value.decode('UTF-8')

    def get_int(self, key: str) -> int:
        """ Parameterize cache from redis to string"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('UTF-8'))
        except Exception:
            value = 0
        return value
