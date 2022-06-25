def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    leftArrOne = getSmaller(arrayOne)
    leftArrTwo = getSmaller(arrayTwo)
    rightArrOne = getBiggerOrEqual(arrayOne)
    rightArrTwo = getBiggerOrEqual(arrayTwo)
    print(leftArrOne, leftArrTwo)
    return sameBsts(leftArrOne, leftArrTwo) and sameBsts(rightArrOne, rightArrTwo)

def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerOrEqual(array):
    bigger = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger
