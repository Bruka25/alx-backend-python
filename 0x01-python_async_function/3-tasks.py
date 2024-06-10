#!/usr/bin/env python3

"""Module for returning async.io task"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task object for the wait_random coroutine
    with the specified max_delay.

    Args:
        max_delay (int): Maximum delay for wait_random coroutine.

    Returns:
        asyncio.Task: Task object for the wait_random coroutine.
    """

    return asyncio.create_task(wait_random(max_delay))
