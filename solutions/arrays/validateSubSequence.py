from typing import Sequence
def isValidSubsequence(array, sequence):
    class SubValidator:
        def __init__(self, inputArr: Sequence[int], seqToValidate: Sequence[int]):
            self.inputArr: Sequence[int] = inputArr
            self.seqToValidate: Sequence[int] = seqToValidate
            self.seqLen = len(self.seqToValidate)
        def validate(self):
            for i, val in enumerate(self.inputArr):
                if val == self.seqToValidate[0]:
                    self.seqToValidate.pop(0)
                    self.seqLen -= 1
                    print(self.seqLen)
                    print(self.inputArr)
                if self.seqLen <= 0:
                    return True
            if self.seqLen > 0:
                return False
    subValidator = SubValidator(array, sequence)
    test = subValidator.validate()
    return test
                