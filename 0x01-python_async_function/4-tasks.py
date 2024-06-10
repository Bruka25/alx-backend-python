#!/usr/bin/env python3


"""Module for executing task and return a sorted list"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes task_wait_random n times and returns a sorted list
       of wait times.

    Args:
        n (int): Number of times to execute the task_wait_random function.
        max_delay (int): Maximum delay for each execution of task_wait_random.

    Returns:
        List[float]: Sorted list of wait times.
    '''

    # Execute task_wait_random n times concurrently using asyncio.gather
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )

    # Sort the list of wait times in ascending order
    return sorted(wait_times)
