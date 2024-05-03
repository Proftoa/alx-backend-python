#!/usr/bin/env python3
"""
Task: 11: Given the parameters and the return values,
add type annotations to the function
"""

from typing import Any, Mapping, Optional, TypeVar, Union

T = TypeVar('T')
Resp = Union[Any, T]
Defl = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defl = None) -> Resp:
    """
    Retrieves a value from a dict using a given key.
    """
    if key in dct:
        return dct[key]
    else:
        return default

