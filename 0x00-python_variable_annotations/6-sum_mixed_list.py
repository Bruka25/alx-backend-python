#!/usr/bin/env python3

"""module for a function returning mixed sum of integers
   and floats
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list containing integers and float numbers."""
    return sum(mxd_lst)
