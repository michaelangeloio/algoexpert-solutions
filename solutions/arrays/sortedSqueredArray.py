def sortedSquaredArray(array):
    sortedArr = [0 for val in array]
    leftIndex = 0
    rightIndex = len(array) - 1
    for i in reversed(range(len(array))):
        leftVal = array[leftIndex]
        rightVal = array[rightIndex]
        if abs(leftVal) > abs(rightVal):
            print(leftVal, rightVal)
            sortedArr[i] = leftVal * leftVal
            leftIndex += 1
        else:
            print(rightVal, leftVal)
            sortedArr[i] = rightVal * rightVal
            rightIndex -= 1
    return sortedArr

