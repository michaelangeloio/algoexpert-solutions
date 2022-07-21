def getPermutations(array):
    # Write your code here.
    if len(array) == 0:
        return []
    if len(array) <= 1:
        return [array.copy()]

    res = []

    for _ in range(len(array)):
        leftOut = array.pop(0)
        perms = getPermutations(array)

        for perm in perms:
            perm.append(leftOut)
        res.extend(perms)
        array.append(leftOut)
    return res
