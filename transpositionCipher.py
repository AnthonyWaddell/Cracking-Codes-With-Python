'''Python program to perform Transposition cipher encryption'''

import pyperclip
def main():
	myMessage = 'Common send is not so common.'
	myKey = 8

	ciphertext = encryptMessage(myKey, myMessage)

	# Print the encrypted message
	print(ciphertext + '|')
	pyperclip.copy(ciphertext)

def encryptMessage(key, message):
	# Each string of the ciphertext represents a column in the grid
	ciphertext = [''] * key

	# Loop through each column of the ciphertext
	for column in range(key):
		currentIndex = column

		# Continue to loop until the currentIndex goes beyond the message length
		while currentIndex < len(message):
			# Place the character at the currentIndex in the message at the
			# end of the current column in the ciphertext
			ciphertext[column] += message[currentIndex]

			# MAdvance currentIndex
			currentIndex += key

	# Convert the ciphertext list into a single string value and return
	return ''.join(ciphertext)

# If transpositionEncrypt.py is run instead of imported as module, call main
if __name__ == '__main__':
	main()