#!/usr/bin/env python3
"""Type annotated function for summing values in a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns string representation of a given float"""
    total: float = 0.0
    for i in range(0, len(input_list) - 1):
        total += input_list[i]

    return total
