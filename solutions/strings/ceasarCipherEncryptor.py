def caesarCipherEncryptor(string, key):
    # Write your code here.
    newLetters = []
    newKey = key % 26
    alphabet = list("a b c d e f g h i j k l m n o p q r s t u v w x y z".replace(" ", ""))
    for letter in string:
        newLetters.append(getNewLetter(letter, newKey, alphabet))
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):
    newLetterCode = alphabet.index(letter) + key
    return alphabet[newLetterCode % 26]
