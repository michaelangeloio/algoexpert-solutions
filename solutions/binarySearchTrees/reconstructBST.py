# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    bst = BST(preOrderTraversalValues[0])
    stack = [bst]
    for i in range(1, len(preOrderTraversalValues)):
        newNode = BST(preOrderTraversalValues[i])
        if newNode.value < stack[-1].value:
            stack[-1].left = newNode
        else:
            parent = None
            while stack and stack[-1].value <= newNode.value:
                parent = stack.pop()
            parent.right = newNode
        stack.append(newNode)
    return bst
