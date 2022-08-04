# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, max_paths):
        self.max_paths = max_paths

def helper(tree, treeInfo):
    if tree is None: return 0
    maxRightPaths = helper(tree.right, treeInfo)
    maxLeftPaths = helper(tree.left, treeInfo)
    paths = maxRightPaths + maxLeftPaths

    if treeInfo.max_paths < paths:
        treeInfo.max_paths = paths
    currentPath = max(maxLeftPaths, maxRightPaths) + 1
    return currentPath

def binaryTreeDiameter(tree):
    # Write your code here.
    treeInfo = TreeInfo(0)
    helper(tree, treeInfo)
    return treeInfo.max_paths
