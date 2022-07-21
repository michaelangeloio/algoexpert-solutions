def runLengthEncoding(string):
    # Write your code here.
    if len(string) == 1:
        return str(1) + string
    encoding = ""
    stringLen = len(string)
    count = 0
    pointer = 0
    for i in range(0, stringLen - 1):
        count += 1
        val = string[i]
        nextVal = string[i + 1]
        if val != nextVal or count == 9:
            print(val, nextVal)
            encoding = encoding + str(count) + val
            count = 0
            pointer = i + 1
        if i + 1 == stringLen - 1:
            encoding = encoding + str(len(string[pointer:])) + nextVal
    return encoding

