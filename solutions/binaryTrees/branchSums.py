from typing import Sequence
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    node = root
    sums: Sequence[int] = []
    getLastLeftLeafs(node, 0, sums)
    print(sums)
    return sums

def getLastLeftLeafs(node: BinaryTree, runningSum: int, sums):
    if node is None:
        return
    branchSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(branchSum)
        return
    getLastLeftLeafs(node.left, branchSum, sums)
    getLastLeftLeafs(node.right, branchSum, sums)
        
    
    
        
        
        
    