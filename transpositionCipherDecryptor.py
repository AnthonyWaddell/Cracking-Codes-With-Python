''' Python module to decrypt transposition cipher encrypted messages'''

#import pyperclip
import math

def main():
	myMessage = 'Cenoonommstmme oo snnio. s s c'
	myKey = 8

	plaintext = decryptMessage(myKey, myMessage)

	# Print the decrypted text
	print(plaintext + '|')
	#pyperclip.copy(plaintext)

def decryptMessage(key, message):
	# Simulate columns and rows of the grid the plaintext was written on
	numColumns = int(math.ceil(len(message) / float(key)))
	numRows = key
	numShadedBoxes = (numColumns * numRows) - len(message)

	# Each string in plaintext reprsents a column in the grid
	plaintext = [''] * numColumns

	# The column and row variables point to the grid location of the next char 
	# in the encrypted message
	column = 0
	row = 0

	for character in message:
		plaintext[column] += character
		column += 1

		# If no more columns or empty bos, move to first column of next row
		if(column == numColumns) or (column == numColumns - 1 and row >= numRows - numShadedBoxes):
			column = 0
			row += 1

	return''.join(plaintext)

# If this is run instead of imported
if __name__ == '__main__':
    main()