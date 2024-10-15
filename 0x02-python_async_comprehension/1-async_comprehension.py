#!/usr/bin/env python3
"""
A Coroutine function that takes no arguments.
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module.
    """
    return [i async for i in async_generator()]
