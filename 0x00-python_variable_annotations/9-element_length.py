#!/usr/bin/env python3
"""
Takes a list mxd_lst of integers and floats and returns
their sum as a float
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes a list mxd_lst of integers and floats
    and returns their sum as a float
    """
    return [(i, len(i)) for i in lst]
