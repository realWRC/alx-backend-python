#!/usr/bin/env python3
"""Duck-typed annotations fix"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that does the thing"""
    if lst:
        return lst[0]
    else:
        return None
