from enum import Enum
from typing import Sequence
class AscDescNeither(Enum):
    ASCENDING = 'ascending'
    DESCENDING = 'descending'
    NEITHER = 'neither'
def isMonotonic(array: Sequence[int]):
    if len(array) <= 2:
        return True
    arrLen: int = len(array)
    el1, el2 = findDiffEl(array, arrLen)
    orderObj = isAscDescOrNeither(el1, el2)
    if orderObj[AscDescNeither.NEITHER]:
        return True
    for i, val in enumerate(array):
        if i == arrLen - 1:
            break
        if orderObj[AscDescNeither.ASCENDING]:
            if val <= array[i + 1]:
                pass
            else:
                return False
        if orderObj[AscDescNeither.DESCENDING]:
            if val >= array[i + 1]:
                pass
            else:
                return False
    return True  
def isAscDescOrNeither(el1: int, el2: int):
    orderObj = {}
    orderObj[AscDescNeither.ASCENDING] = False
    orderObj[AscDescNeither.DESCENDING] = False
    orderObj[AscDescNeither.NEITHER] = False
    if el2 > el1:
        orderObj[AscDescNeither.ASCENDING] = True
    elif el2 < el1:
        orderObj[AscDescNeither.DESCENDING] = True
    else:
        orderObj[AscDescNeither.NEITHER] = True
    return orderObj
def findDiffEl(array: Sequence[int], arrLen: int):
    found = False
    i = 0
    while not found:
        if i == arrLen - 1:
            found = True
            return array[-2], array[-1]
        if array[i + 1] - array[i] > 1:
            return array[i], array[i + 1]
        i += 1
