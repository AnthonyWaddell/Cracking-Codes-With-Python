''' Simple python program to encrypt and decrypt files using transposition cipher 
	module. Requires having the encrypting and decrypting file to import.'''

import transpositionCipher
import transpositionCipherDecryptor
import os
import sys
import time

def main():
	inputFilename = 'frankenstein.txt'
	outputFilename = 'frankenstein.encrypted.txt'
	myKey = 10
	# Can be 'encrypt' or 'decrypt'
	myMode = 'encrypt'

	# If the provided file does not exist, exit
	if not os.path.exists(inputFilename):
		print('Input file name: ' + inputFilename + ' does not exist...')
		sys.exit()

	# Double check that output file will not overwrite an existsing file
	if os.path.exists(outputFilename):
		print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))
		response = ipnut('>')
		if not response.lower().startswith('c'):
			sys.exit()

	# Read from input file
	fileObj = open(inputFilename)
	cont = fileObj.read()
	fileObj.close()

	print('%sing...' % (myMode.title()))

	# Measure how long the process will take
	startTime = time.time()
	if myMode == 'encrypt':
		translated = transpositionCipher.encryptMessage(myKey, content)
	elif myMode == 'decrypt':
		translated = transpositionCipherDecryptor.decryptMessage(myKey, content)
	totalTime = round(time.time() - startTime, 2)
	print('%sion time: %s seconds' % (myMode.title(), totalTime))

	# Write traslated content to the output file:
	outputFileObj = open(outputFilename, 'w')
	outputFileObj.write(translated)
	outputFileObj.close()

	print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
	print('%sed file is %s.' % (myMode.title(), outputFilename))

# If this file is ran instead of imported
if __name__ == '__main__':
	main()
