#! python3
''' Simple python module used in conjunction with a text file containing every word in
	the english language. Used with cypher decryptors that have a significant number 
	of possible keys.'''

# To use, type: import detectEnglish
# Returns true or false
# Requires dictionary.txt in current working directory

UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'

def loadDictionary():
	dictionaryFile = open('dictionary.txt')
	englishWords = {}
	for word in dictionaryFile.read.split('\n'):
		englishWords[word] = None
	dictionaryFile.close()
	return englishWords

ENGLISH_WORDS = loadDictionary(message)

# Count the number of possible matching words
def getEnglishCount(message):
	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()

	# Return false if nothing is found
	if possibleWords == []:
		return 0.0

	matches = 0
	for word in possibleWords:
		if word in ENGLISH_WORDS:
			matches += 1
	return float(matches) / len(possibleWords)

# Trim content to just letters and spaces
def removeNonLetters(message):
	lettersOnly = []
	for character in message:
		if character in LETTERS_AND_SPACE:
			lettersOnly.append(character)
	return ''.join(lettersOnly)

# 20 percent of words must exist in dictionary
# 85% of characters must be letters or spaces
def isEnglish(message, wordPercentage = 20, letterPercentage = 85):
	wordsMatch = getEnglishCount(message) * 100 >= wordPercentage
	numLetters = len(removeNonLetters(message))
	messageLetterPercentage = float(numLetters) / len(message) * 100
	lettersMatch = messageLetterPercentage >= letterPercentage
	return wordsMatch and lettersMatch