#!/usr/bin/env python3


"""Module for python random python random delay"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0
    and max_delay seconds and then returns the delay.

    Args:
        max_delay (int): Maximum delay in seconds (default is 10).

    Returns:
        float: The actual delay time that the coroutine waited.
    """

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
