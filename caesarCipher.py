''' Simple python program for the caesar cipher'''

import pyperclip.py

message = "This is my secret message"
translated = ""
key = 13

# can be eithe r'encrypt' or 'decrypt'
mode = 'encrypt'

# Everything we can encrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for character in message:
	if character in SYMBOLS:
		symbolIndex = SYMBOLS.find(character)

		# encrypt/decrypt
		if mode == 'encrypt':
			translatedIndex = symbolIndex + key

		elif mode == 'decrypt':
			translatedIndex = symbolIndex - key

		# In the event of wraparound
		if translatedIndex >= len(SYMBOLS):
			translatedIndex -= len(SYMBOLS)
		elif translatedIndex < 0:
			translatedIndex += len(SYMBOLS)

		translated += SYMBOLS[translatedIndex]

	else:
		# Append the symbol without encrypting or decrypting
		translated += character

# Output the string
print(translated)
pyperclip.copy(translated)
