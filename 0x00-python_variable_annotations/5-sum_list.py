#!/usr/bin/env python3

"""Module which takes list of floats as an argument and 
   returns their sum as a float
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of float numbers."""
    return sum(input_list)
