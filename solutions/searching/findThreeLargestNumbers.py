def findThreeLargestNumbers(array):
    # Write your code here.
    print(array)
    three = []
    for _ in range(3):
        largest = max(array)
        three.append(largest)
        array.remove(max(array))
    return sorted(three)
