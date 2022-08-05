# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    if node.right:
        return findNext(node.right, node)
    if node.parent:
        return findNext(node.parent, node, reverse = True)
    return None

def findNext(node, targetNode, reverse = False):
    if reverse:
        if node.right == targetNode:
            if node.parent:
                return findNext(node.parent, targetNode, reverse=True)
            else:
                return None
        return node
    if node.left:
        return findNext(node.left, targetNode)
    return node
