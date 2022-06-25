# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return isValid(tree, float("-inf"), float("inf"))

def isValid(node, minValue: int, maxValue: int) -> bool:
    if node is None:
        return True
    print("investigating ", node.value, minValue, maxValue)
    if node.value >= maxValue or node.value < minValue:
        return False
    leftIsValid = isValid(node.left, minValue, node.value)
    return leftIsValid and isValid(node.right, node.value, maxValue)
    
