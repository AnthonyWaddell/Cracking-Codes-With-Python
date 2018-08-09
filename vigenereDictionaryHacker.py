''' Dictionary hacker for a vigenere cipher. Won't work on random-letter keys'''

import detectEnglish
import vigenereCipher
import pyperclip

def main():
	ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
	hackedMessage = hackVigenereDictionary(ciphertext)

	if hackedMessage != None:
		print('Copying hacked message to clipboard...')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Failed to hack encryption.')

def hackVigenereDictionary(ciphertext):
	fo = open('dictionary.txt')
	words = fo.readlines()
	fo.close

	for word in word:
		# Remove newline
		word = word.strip()
		decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
		if detectEnglish.isEnglish(decryptedText, wordPercentage = 40):
			# Check with user to see if key has been found
			print()
			print("owo what's this? *notices possible encryption break*")
			print('Key ' + str(word) + ': ' + decryptedText[:100])
			print()
			print('Enter D for done, or just press enter to continue...')
			response = input('>')

			if response.upper().startswith('D'):
				return decryptedText

if __name__ == '__main__':
	main()