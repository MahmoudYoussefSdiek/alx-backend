#!/usr/bin/env python3
"""
This module contains a function that calculates the
start and end index for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Function to calculate the start and end index for pagination.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
