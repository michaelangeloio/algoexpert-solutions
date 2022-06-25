from typing import Sequence, Dict
def fourNumberSum(array, targetSum):
    sumMap = {}
    finalMap = buildSumMap(array, sumMap)
    sumArrs = []
    keyMap = list(finalMap.keys())
    for i, key in enumerate(keyMap):
        for i2, key2 in enumerate(keyMap):
            if key != key2:
                if key + key2 == targetSum:        
                    for arr in finalMap[key]:
                        for arr2 in finalMap[key2]:
                            arrSet = set(arr + arr2)
                            if len(set(arrSet)) == 4 and arrSet not in sumArrs:
                                sumArrs.append(arrSet)
    finalArrs = []
    for dist in sumArrs:
        returnArr = []
        for i in dist:
            returnArr.append(array[i])
        finalArrs.append(returnArr)
        
    return finalArrs
    pass

def buildSumMap(array: Sequence[int], sumMap):
    for i, val in enumerate(array):
        for i2, val2 in enumerate(array):
            if val != val2:
                binarySum: int = val + val2
                if binarySum not in sumMap:
                    sumMap[binarySum] = [[i, i2]]
                else:
                    keyVal = sumMap.get(binarySum)
                    for arr in keyVal:
                        if checkIndexes(arr, [i,i2], binarySum):
                            if [i, i2] not in keyVal and [i2, i] not in keyVal:
                                sumMap[binarySum].append([i,i2])
    return sumMap

def checkIndexes(array: Sequence[int], compareArray: Sequence[int], sum: int):
    set1 = set(array)
    set2 = set(compareArray)
    if set1 == set2:
        return False
    else:
        return True