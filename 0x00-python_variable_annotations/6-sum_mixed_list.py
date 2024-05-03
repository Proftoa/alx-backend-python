#!/usr/bin/env python3
"""
Task 6: Write a type-annotated function sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mixed_list: List[Union[int, float]]) -> float:
    """
    Compute the sum of a list of integers and floating-point numbers.
    """
    total = 0.0
    for num in mixed_list:
        total += num
    return total

