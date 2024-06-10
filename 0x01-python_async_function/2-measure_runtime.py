#!/usr/bin/env python3

"""Module to measure the runtime of concurrent coroutines"""

import asyncio
import time
from typing import Tuple

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay), and returns the
    average time per call.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        float: The average time per call.
    """

    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n coroutine
    end_time = time.time()  # Record the end time

    total_time = end_time - start_time  # Calculate the total elapsed time
    return total_time / n  # Return the average time per call
