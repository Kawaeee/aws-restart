# Take three arguments: the message, the cipherKey, and the alphabet.
# Initialize variables.
# Use a for loop to traverse each letter in the message.
# For a specific letter, find the position.
# For a specific letter, determine the new position given the cipher key.
# If current letter is in the alphabet, append the new letter to the encrypted message.
# If current letter is not in the alphabet, append the current letter.
# Return the encrypted message after exhausting all the letters in the message.

def getDoubleAlphabet():
    alphabet = input("Please enter alphabet: ")
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

def runCaesarCipherProgram():
    myAlphabet = getDoubleAlphabet() # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(f'Alphabet: {myAlphabet}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet)
    print(f'Decypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()