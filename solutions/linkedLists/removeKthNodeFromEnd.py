# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    node = head
    totalNodes: int = 0
    while node.next is not None:
        totalNodes += 1
        node = node.next
    node2 = head
    counter: int = 0
    while node2.next is not None:
        counter += 1
        if (totalNodes - (k - 1)) == counter:
            if node2.next.next is not None:
                node2.next = node2.next.next
            else:
                node2.next = None
                break
        node2 = node2.next
    if k > totalNodes:
        temp = head
        temp.value = head.next.value
        temp.next = head.next
        head.next = head.next.next
    # use this to verify 
    verify = head
    while verify.next is not None:
        print(verify.value)
        verify = verify.next
