from typing import Sequence
def moveElementToEnd(array, toMove):
    integerMover = IntegerMover(array, toMove)
    test = integerMover.moveIntsToBack()
    return test
class IntegerMover: 
    def __init__(self, arr: Sequence[int], toMove: int ):
        self.arr: Sequence[int] = arr
        self.toMove: int = toMove
    def moveIntsToBack(self):
        toMoveCount: int = 0
        arrLen = len(self.arr)
        indexCollection = []
        for i, val in enumerate(self.arr):
            if val == self.toMove:
                indexCollection.append(i)
                toMoveCount += 1 
        for index in sorted(indexCollection, reverse = True):
            print(self.arr)
            self.arr.pop(index)
        return self.arr + [self.toMove for val in range(0, toMoveCount)]
