#!/usr/bin/env python3
"""This module defines a function `measure_runtime`"""
from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Define the measure_runtime coroutine"""
    startTime = time()
    tasks = [async_comprehension() for i in range(4)]
    await gather(*tasks)
    endTime = time()
    return (endTime - startTime)
