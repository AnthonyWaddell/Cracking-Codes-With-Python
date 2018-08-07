''' Substitution cipher hacker that uses word patterns to decrypt. Must run 
	makeWordPattersns.py first to create wordPatterns.py module. Additionally,
	requires dictionary.txt'''

#import wordPatterns.py
# if ^^ gives ModuleNotFoundError, input the following
#import sys
#sys.path.append('Folder_where_wordPatterns_is)

import os
import re
import copy
import pyperclip
import simpleSubCipher
import wordPatterns
import makeWordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
	message = '''Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr
        sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa
        sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac
        ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx
        lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia
        rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh.
        -Facjclxo Ctrramm'''

    # Determine the possible valid ciphertext translations
    print('Attempting to hack....')
    letterMapping = hackSimpleSub(message)

    # Display to user
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacked message to clipboard:')
    hackedMessage = decryptWithCipherLetterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)

def getBlankCipherLetterMapping():
	return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
    'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
    'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
    'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

''' Takes a dictionary value that stores a cipherletter mapping, 
	which is copied by the function. The cipherword parameter is 
	a string value of the ciphertext word. The candidate parameter
	is a possible English word that the cipherword could decrypt
	tp. This function adds the letters in the candidate as
	potential decryption letters for the cipherletters in the
	cipherletter mapping '''
def addLettersToMapping(letterMapping, cipherword, candidate):
	for i in range(len(cipherword)):
		if candidate[i] not in letterMapping[cipherword[i]]:
			letterMapping[cipherword[i]].append(candidate[i])

''' To intersect two maps, create a blank map and then add only the 
	potential decryption letters if they exist in BOTH maps'''
def intersectMappings(mapA, mapB):
	intersectedMapping = getBlankCipherLetterMapping()
	for letter in LETTERS:
		# An empty list means any letter is possible. In this case
		# just copy the other map entirely
		if mapA[letter] == []:
			intersectedMapping[letter] = copy.deepcopy(mapB[letter])
		elif mapB[letter] == []:
			intersectedMapping[letter] = copy.deepcopy(mapA[letter])
		else:
			# If a letter in mapA[letter] exists in mapB[letter], add
			# that letter to intersectedMapping[letter]
			for mappedLetter in mapA[letter]:
				if mappedLetter in mapB[letter]:
					intersectedMapping[letter].append(mappedLetter)

	return intersectedMapping

''' Cipherletters in the mapping that map to only one letter are 'solved'
	and can be removed from the other letters. EX: if 'A' maps to potential
	letters ['M', 'N'] and 'B' maps to ['N'], we know that 'B' must map to 'N'
	so we can remove 'N' from the list of what 'A' could map to.'''
def removedSolvedLettersFromMapping(letterMapping):
	loopAgain = True
	while loopAgain:
		loopAgain = False

		# Solved letters will be a list of uppercase letters that have one
		# and only one possible mapping in letterMapping
		solvedLetters = []
		for cipherletter in LETTERS:
			if len(letterMapping[cipherletter]) == 1:
				solvedLetters.append(letterMapping[cipherletter][0])

		# If a letter is solved, it can't be a match for oher ciphertext
		# letters
		for cipherletter in LETTERS:
			for s in solvedLetters:
				if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
					letterMapping[cipherletter].remove(s)
					if len(letterMapping[cipherletter]) == 1:
						# A new letter is solved, so loop again
						loopAgain = True

	return letterMapping

def hackSimpleSub(message):
	intersectedMap = getBlankCipherLetterMapping()
	cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()
	for cipherword in cipherwordList:
		# Get a new cipherletter mapping for each ciphertext worfd
		candidateMap = getBlankCipherLetterMapping()

		wordPattern = makeWordPatterns.getWordPattern(cipherword)
		if wordPattern not in wordPatterns.allPatterns:
			continue

		# Add the letters of each candidate to the mapping
		for candidate in wordPatterns.allPatterns[wordPattern]:
			addLettersToMapping(candidateMap, cipherword, candidate)

		# Intersect thenew mapping with the existing intersected mapping
		intersectedMap = intersectMappings(intersectedMap, candidateMap)

	# Remove any solved letters from the other lists
	return removedSolvedLettersFromMapping(intersectedMap)

def decryptWithCipherLetterMapping(ciphertext, letterMapping):
	# Return a string of the ciphertext decrypted with the letter mapping, 
	# with any ambiguous decrypted letters replaced with an underscore

	# First create a simple sub key from the letterMapping mapping
	key = ['x'] * len(LETTERS)
	for cipherletter in LETTERS:
		if len(letterMapping[cipherletter]) == 1:
			# If there's only one letter, add it to the key:
			keyIndex = LETTERS.find(letterMapping[cipherletter][0])
			key[keyIndex = cipherletter]
		else:
			ciphertext = ciphertext.replace(cipherletter.lower(), '_')
			ciphertext = ciphertext.replace(cipherletter.upper(), '_')
	key = ''.join(key)

	# Now, with the key, decrypt the ciphertext
	return simpleSubCipher.decryptMessage(key, ciphertext)

if __name__ == '__main__':
	main()