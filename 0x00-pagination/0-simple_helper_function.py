#!/usr/bin/env python3

"""
    Defines a function named index range
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
        Returns a tuple of size two containing a start index and an end index
    """
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex