''' Python module that can break a message encrypted using an affine cipher'''

import pyperclip
import detectEnglish
import affineCipher
import cryptomath

SILENT_MODE = False

def main():
	myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!A
          uaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1
          iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
    	# Display plaintext
    	print('Coopying hacked message to the clipboard')
    	print(hackedMessage)
    	pyperclip.copy(hackedMessage)
	else:
		print('Failed to hack message')

def hackAffine(message):
	print('Attempting to hack message...')
	print('To quit any time prss CTRL-C (Windows) or  CTRL-D (macOS && Linux')

	# Begin the brute-force of every key
	for key in range(len(affineCipher.SYMBOLS) ** 2):
		keyA = affineCipher.getKeyParts(key)[0]
		if cryptomath.gcd(keyA, len(affineCipher.SYMBOLS)) != 1:
			continue

			decryptedText = affineCipher.decryptMessage(key, message)
			if not SILENT_MODE:
				print('Treid Key %s... (%s)' % (key, decryptedText[:40]))

			if detectEnglish.isEnglish(decryptedText):
				# Ask user is decrypted key was found
				print()
				print('Possible encryption hack...')
				print('Key: %s' % (key))
				print('Decrypted message: ' + decryptedText[:200])
				print()
				print('Enter D for done, or ENTER to continue hacking')
				response = input('>')

				if response.strip().upper().startswith('D'):
					return decryptedText
	return None

# IF ran as run instead of imported
if __name__ == '__main__':
	main()