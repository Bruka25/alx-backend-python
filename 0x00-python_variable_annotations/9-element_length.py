#!/usr/bin/env python3


"""Module for annotating function parameters with the appropriate
   types
"""

from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """Returns a list of tuples where each tuple contains an element from
       lst and its length.
    """
    return [(i, len(i)) for i in lst]
