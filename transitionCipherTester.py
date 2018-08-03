''' Automate the testing of the transition cipher'''

import transpositionCipher.py
import transpositionCipherDecryptor.py
import sys
import random

def main():
	random.seed(42)

	# Run 20 tests
	for i in range(20):

		# Generate random messages of random length
		message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

		# Convert message to list and shuffle
		message = list(message)
		random.shuffle(message)
		message = ''.join(message)

		print('Test # %s: %s...' % (i + 1, message[:50]))

		# Check for all possible keys for each message
		for key in range(1, int(len(message) / 2)):
			encrypted = transpositionCipher.encryptMessage(key, message)
			decrypted = transpositionCipherDecryptor.decryptMessage(key, encrypted)

			# If the decryption doesn't match the original message
			if message != decrypted:
				print('Mismatch with key: %s and message %s' % (key, message))
				print('Decrypted as: ' + decrypted)
				sys.exit()

	print("Transposition cipher test passed...")

if __name__ == '__main__':
	main()