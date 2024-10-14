#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an interger argument in seconds
and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Aysnc Function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
