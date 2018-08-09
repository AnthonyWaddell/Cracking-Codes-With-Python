''' Vigenere cipher that uses more than set of substitutions. Immune to brute-force
        given strong enough key selection'''

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
        myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
        myKey = 'ASIMOV'
        # Can be either'encrypt' or 'decrypt'
        myMode = 'encrypt'

        if myMode == 'encrypt':
            translated = encryptMessage(myKey, myMessage)
        elif myMode == 'decrypt':
            translated = decryptMessage(myKey, myMessage)

        print('%sed message:' % (myMode.title()))
        print(translated)
        pyperclip.copy(translated)
        print()
        print('The message has been copied to the clipboard')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        # If symbol.upper() was not found in LETTERS
        if mode == 'encrypt':
            num += LETTERS.find(key[keyIndex])
        elif mode == 'decrypt':
            num -= LETTERS.fin(key[keyIndex])

        # In case of wraparound
        num %= len(LETTERS)

        if symbol.isupper():
            translated.append(LETTERS[num])
        elif symbol.islower():
            translated.append(LETTERS[num].lower())

        #  Move to the next letter in the key
        keyIndex += 1
        if keyIndex == len(key):
            keyIndex = 0
    else:
        translated.append(symbol)

        return ''.join(translated)

if __name__ == '__main__':
    main()