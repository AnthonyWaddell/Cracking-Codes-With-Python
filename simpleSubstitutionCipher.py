''' Simple substitution cipher that contains enough keys that it 
	can thwart a bruteforce attack'''

import sys
import random
import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	myMessage = '''If a man is offered a fact which goes against his
        instincts, he will scrutinize it closely, and unless the evidence
        is overwhelming, he will refuse to believe it. If, on the other
        hand, he is offered something which affords a reason for acting
        in accordance to his instincts, he will accept it even on the
        slightest evidence. The origin of myths is explained in this way.
        -Bertrand Russell'''

    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    # Can be 'encrypt' or 'decrypt'
    myMode = 'encrypt'

    if keyIsValid(myKey):
      	sys.exit('There is an error in the key or symbol set')
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
    	translated = decryptMessage(myKey, myMessage) 
    print('Using Key: %s' % (myKey))
	print('The %sed message is:' % (myMode))
	print(translated)
	pyperclip.copy(translated)
	print('This message has been copied to clipboard.')

def keyIsValid(key):
	keyList = list(key)
	lettersList = list(LETTERS)
	keyList.sort()
	lettersList.sort()

	return keyList == lettersList

def encryptMesage(key, message):
	return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
	return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
	translated = ''
	charsA = LETTERS
	charsB = key

	if mode == 'decrypt':
		# If decrypting, only have to swap LETTERS with KEY
		charA, charsB = charsB, charsA

	# Loop over each symbol
	for symbol in message:
		if symbol.upper() in charsA:
			# Encrypt or decrypt
			symIndex = charsA.find(symbol.upper())
			if symbol.isupper():
				translated += charsB[symIndex].upper()
			else:
				translated += charsB[symIndex].lower()
		else:
			# If symbol is not in letters, just append it
			translated += symbol

	return translated

def getRandomKey():
	key = list(LETTERS)
	random.shuffle(key)
	return ''.join(key)

# If ran instead of imported
if __name__ == '__main__':
	main()