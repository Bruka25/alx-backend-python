#!/usr/bin/env python3


"""Module that will collect  10 random numbers and
   return 10 random number"""

from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    A coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [number async for number in async_generator()]
