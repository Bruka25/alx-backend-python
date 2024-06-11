#!/usr/bin/env python3


"""Module for a coroutine called async_generator that takes no arguments"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random number between 0 and 10.

    This generator runs a loop 10 times. Each iteration, it asynchronously
    waits for 1 second, then yields a random float number between 0 and 10.
    """
    for _ in range(10):  # Loop 10 times
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
