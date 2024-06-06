#!/usr/bin/env python3


"""Module for annotating function parameters with the appropriate
   types
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Computes the length of a list of sequences
    '''
    return [(i, len(i)) for i in lst]
