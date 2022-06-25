
def isPalindrome(string: str):
    stringLen: int = len(string)
    if stringLen == 2: 
        return False
    right: int = stringLen - 1
    for left, leftEl in enumerate(string):
        if right - left <= 1:
            return True
        if leftEl != string[right]:
            return False
        right -= 1
