#!/usr/bin/env python3


"""Module for concurrent coroutines"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Spawns wait_random n times with the specified max_delay and returns the
    list of all delays in ascending order without using sort().

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        list: List of delays in ascending order.
    """
    # Create a list to store the delays.
    delays = []

    # Create a list of tasks for n calls to wait_random.
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    # Await each task and insert the result into the delays
    # list in sorted order
    for task in tasks:
        delay = await task

        # Insert the delay in the correct position to maintain ascending order
        for i, existing_delay in enumerate(delays):
            if delay < existing_delay:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)

    return delays
