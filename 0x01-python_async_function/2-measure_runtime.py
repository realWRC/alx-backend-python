#!/usr/bin/env python3
"""
Async routine that returns the list of all the delays (float values)
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that uses other async functions
    """
    startTime = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.perf_counter()

    totalTime = endTime - startTime
    return (totalTime/n)
