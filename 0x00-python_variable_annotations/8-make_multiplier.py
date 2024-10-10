#!/usr/bin/env python3
"""
Takes a list mxd_lst of integers and floats and returns
their sum as a float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
