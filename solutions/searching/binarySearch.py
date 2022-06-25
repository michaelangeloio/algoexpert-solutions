def binarySearch(array, target):
    # Write your code here.
    return search(array, target, 0, len(array) - 1)

def search(array, target, left, right):
    while left <= right:
        print(left, right)
        i = (left + right) // 2
        matchMaybe = array[i]
        if target == matchMaybe:
            return i
        elif target < matchMaybe:
            right = i - 1
        else:
            left = i + 1
    return -1
        
