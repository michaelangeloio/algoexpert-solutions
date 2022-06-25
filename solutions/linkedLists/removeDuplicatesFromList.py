class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None  

def removeDuplicatesFromLinkedList(linkedList):
    newNode = LinkedList(linkedList.value)
    return helper(linkedList)
    # Write your code here.

def helper(val):
    node = val
    while node is not None: 
        soloNode = node.next
        if soloNode is not None:
                while soloNode is not None and soloNode.value == node.value:
                    print(soloNode.value)
                    soloNode = soloNode.next
        node.next = soloNode
        node = node.next
    return val
        
        
        


        
