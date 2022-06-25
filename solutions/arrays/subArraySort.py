from typing import Dict
def subarraySort(array):
    # Pretty sure this is O(n) time, not sure about O(n) space
    descMap: Dict[int: int] = {}
    arrLen = len(array)
    for i in range(len(array) - 1):
        val = array[i]
        nextVal = array[i + 1]
        i2 = i + 1
        if nextVal < val:
            descMap[i2] = nextVal
        if arrLen > 2:
            prevVal = array[i - 1]
            if prevVal == val and (i - 1) in descMap:
                descMap[i] = val
            if nextVal in descMap.values():
                descMap[i2] = nextVal
    keys = list(descMap.keys())
    keysLen = len(keys)
    if keysLen == 0:
        return [-1, -1]
    minKey = min(descMap, key=descMap.get)
    minVal = descMap[minKey]
    minIndex = firstIndex(array, minVal)
    if keysLen == 1:
        highestVal = [i for i, val in enumerate(array) if array[keys[0] - 1] < val]
        if len(highestVal) == 0:
            return [minIndex, arrLen - 1]
        return[minIndex, highestVal[0] - 1]
    highestKey = max(keys)
    lowestKey = min(keys)
    return[minIndex, highestKey]
    
def firstIndex(array, min: int):
    for i, val in enumerate(array):
        if min < val:
            return i
