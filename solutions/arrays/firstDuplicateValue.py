def firstDuplicateValue(array):
    dupMap = {}
    arrLen = len(array)
    for i, val in enumerate(array):
        if val not in dupMap:
            dupMap[val] = [i]
        elif val in dupMap:
            return val
    return -1
    
