def nodeDepths(root):
    # Write your code here.
    branchEnds = []
    sums = []
    helperLeft(root, branchEnds, sums)
    helperRight(root, branchEnds, sums)
    return sum(sums)


def helperLeft(root, branchEnds, sums, count = 0):
    leftNode = root

    while leftNode.left is not None:
        count += 1
        if leftNode.right is not None:
            helperLeft(leftNode.right, branchEnds, sums, count)
        leftNode = leftNode.left
        if leftNode.left is None:
            if leftNode.value in branchEnds:
                continue
            else:
                sums.append(count)
                count = 0
                branchEnds.append(leftNode.value)
def helperRight(root, branchEnds, sums, count = 0):
    rightNode = root 
    while rightNode.right is not None:
        count += 1
        if rightNode.left is not None:
            helperRight(rightNode.left, branchEnds, sums, count)
        rightNode = rightNode.right
        if rightNode.right is None:
            if rightNode.value in branchEnds:
                continue
            else:
                sums.append(count)
                count = 0
                branchEnds.append(rightNode.value)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
