def selectionSort(array):
    # Write your code here.
    cIdx = 0
    while cIdx < len(array) - 1:
        sIdx = cIdx
        for i in range(cIdx + 1, len(array)):
            if array[sIdx] > array[i]:
                sIdx = i
        swap(cIdx, sIdx, array)
        cIdx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
