#!/usr/bin/env python3

"""Module for that measures the runtime"""

import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that measures the total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.

    Returns the total runtime in seconds.
    """
    start_time = time.perf_counter()  # Record the start time
    await asyncio.gather(*(async_comprehension() for _ in range(4)))  # Execute four async_comprehension coroutines in parallel
    end_time = time.perf_counter()  # Record the end time
    return end_time - start_time  # Calculate and return the total runtime
