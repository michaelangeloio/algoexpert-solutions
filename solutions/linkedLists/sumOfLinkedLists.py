from typing import Sequence
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def insert(self, arr):
        currentNode = self
        for val in arr:
            currentNode.next = LinkedList(val)
            currentNode = currentNode.next

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    reversedarr1 = reverseArr(helper(linkedListOne))
    reversedarr2 = reverseArr(helper(linkedListTwo))
    combinedNumStrings = combineNums([reversedarr1, reversedarr2])
    total = 0
    for numString in combinedNumStrings:
        total += int(numString)
    totalString = str(total)
    newLinkedList = LinkedList(totalString[0])
    stringArr = [int(totalString[i]) for i in reversed(range(0, len(totalString)))]
    newLinkedList.insert(stringArr)
    node = newLinkedList.next
    while node is not None:
        print(node.value)
        node = node.next
    return newLinkedList.next

def helper(linkedList):
    arr: Sequence[int] = []
    if linkedList is None:
        return []
    arr.append(linkedList.value)
    nextNode = linkedList.next
    while nextNode is not None:
        arr.append(nextNode.value)
        nextNode = nextNode.next
    return arr

def reverseArr(arr: Sequence[int]):
    reversedArr = []
    arrLen = len(arr)
    for i in reversed(range(0, arrLen)):
        reversedArr.append(arr[i])
    return reversedArr

def combineNums(arrs: Sequence[Sequence[int]]):
    combinedNums: Sequence[str] = []
    for arr in arrs:
        numString = ''
        for num in arr:
            numString = numString + str(int(num))
        combinedNums.append(numString)
    return combinedNums
    
        
