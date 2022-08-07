from collections import Counter
def generateDocument(characters, document):
    # Write your code here.
    charCounter = Counter(characters)
    docCounter = Counter(document)

    for key, value in docCounter.items():
        if key in charCounter:
            if value > charCounter[key]:
                return False
        else:
            return False
    return True
