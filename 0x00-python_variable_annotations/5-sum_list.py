#!/usr/bin/env python3
"""Type annotated function for summing values in a list"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums values in a list of floats"""
    return float(sum(input_list))
