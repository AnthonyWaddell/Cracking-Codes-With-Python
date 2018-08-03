''' Simple python program to bruteforce a caesar cipher'''

''' Simple python program for the caesar cipher'''


# Example string
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

# Everything we can encrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
	# try again with each key attempt
	translated = ""

	for character in message:
		if character in SYMBOLS:
			symbolIndex = SYMBOLS.find(character)
			translatedIndex = symbolIndex - key

			# In the event of wraparound
			if translatedIndex < 0:
				translatedIndex += len(SYMBOLS)

			translated += SYMBOLS[translatedIndex]

		else:
			# Append the symbol without encrypting or decrypting
			translated += character

	# Output each attempt
	print('Key # %s: %s' % (key, translated))