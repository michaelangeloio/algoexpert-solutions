def firstNonRepeatingCharacter(string):
    # Write your code here.
    for idx in range(len(string)):
        if string[idx] not in string[:idx]+string[idx+1:]:
            return idx
    return -1
