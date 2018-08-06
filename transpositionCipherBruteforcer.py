''' Brute force approach to hacking a transposition cipher. Used in conjunction with
	detectEnglish.py to recognize a correct key.'''

import detectEnglish
import transpositionCipherDecryptor
import pyperclip

def main():
	myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh
          na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
          euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain
          one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp
          ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh
          gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
          aBercaeu thllnrshicwsg etriebruaisss  d iorr."""

    hackedMessage = hackTransposition(myMessage)

    if hackedMessage == None:
        print('Failed to hack encryption...')
    else:
    	print('Copying hacked message to clipboard...')
    	print(hackedMessage)
    	pyperclip.copy(hackedMessage)

def hackTransposition(message):
	print('Attempting to hack message...')
	print('Press CTRL-C on Windows or CTRL-D on macOS or Linux to cancel....')

	# Loop over every key
	for key in range(1, len(message)):
		print('Attempting key #%s' % (key))

		decryptedText = transpositionCipherDecryptor.decryptMessage(key, message)

		if(detectEnglish.isEnglish(decryptedText)):
			# Ask if this is correct decryption
			print();
			print('Possible encryption hack:')
			print('Key %s: %s' % (key, decryptedText[:100]))
			print()
			print('Please enter D if done, anything else to continue hacking attenmpts:')
			response = input('>')

			if response.strip().upper.startswith('D'):
				return decryptedText

	# If hack failed
	return None

if __name__ == '__main__':
	main()