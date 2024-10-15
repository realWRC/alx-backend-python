#!/usr/bin/env python3
"""
A Coroutine function that takes no arguments.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    endTime = time.time()
    return (endTime - startTime)
