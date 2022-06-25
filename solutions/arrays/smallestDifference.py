def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    print(arrayOne)
    print(arrayTwo)
    arr1Map = {}
    arr2Map = {}
    finalArr = [arrayOne[0], arrayTwo[0]]
    minDiff = abs(arrayOne[0] - arrayTwo[0])
    arr = arrayOne + arrayTwo 
    arr.sort()
    for val in arrayOne:
        arr1Map[val] = True
    for val in arrayTwo:
        arr2Map[val] = True
    i = 0 
    arrLen = len(arr)
    while i < (arrLen - 1):
        currentVal = arr[i]
        nextVal = arr[i+1]
        newDiff = abs(nextVal - currentVal)
        if newDiff < minDiff:
            if (currentVal in arr1Map and nextVal in arr2Map):
                minDiff = newDiff
                finalArr = [currentVal, nextVal]
            elif (nextVal in arr1Map and currentVal in arr2Map):
                minDiff = newDiff
                finalArr = [nextVal, currentVal]
        i +=1
    return finalArr
    