from typing import Sequence
def threeNumberSum(array: Sequence[int], targetSum):
    array.sort()
    arrayLen: int = len(array)
    finalArrs: Sequence[Sequence[int]] = []
    for i in range(0, arrayLen - 1):
        left: int = i + 1
        right: int = arrayLen - 1
        while left < right:
            sum: int = array[i] + array[left] + array[right]
            if sum == targetSum:
                finalArrs.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            if sum < targetSum:
                left += 1
            if sum > targetSum:
                right -= 1
    return finalArrs
    pass
