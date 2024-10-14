#!/usr/bin/env python3
"""
Async routine that returns the list of all the delays (float values)
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that takes and integer and returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
