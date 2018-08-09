''' Frequency analysis to determine the frequency of each English letter in a particular
	text. Compare these frequencies to the frequency of letters in ciphertext to
	help break encryptions'''

#import pyperclip

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Create a dictionary with keys for each letter and values being their frequency
def getLetterCount(message):
	letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
        'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
        'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
        'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

        for letter in message.upper():
    		if letter in LETTERS:
    			letterCount[letter] += 1

	return letterCount

def getItemAtIndexZero(items):
	return items[0]

# Returns a string of letters from most frequent to least frequent
def getFrequencyOrder(items):
	# Get a dictionary of each letter and their count
	letterToFreq = getLetterCount(message)
	# Make a dictionary of each frequency count to the letter(s)
	freqToLetter = {}
	for letter in LETTERS:
		if letterToFreq[letter] not in freqToLetter:
			freqToLetter[letterToFreq[letter]] = [letter]
		else:
			freqToLetter[letterToFreq[letter]].append(letter)

	# Put each of the letters in reverse "ETAOIN" order and convert to string
	for freq in freqToLetter:
		freqToLetter[freq].sort(key = ETAOIN.find, reverse = True)
		freqToLetter[freq] = ''.join(freqToLetter[freq])

	# Convert the freqToLetter dictionary to a list of tuple pairs and sort
	freqPairs = list(freqToLetter.items())
	freqPairs.sort(key = getItemAtIndexZero, reverse = True)

	# Letters sorted by frequency, now turn to string
	freqOrder = []
	for freqPair in freqPairs:
		freqOrder.append(freqPair[1])

	return ''.join(freqOrder)

# Return the the number of matches the string passed in has when its letter 
# frequency is compared against English letter frequency. Matching based
# on how many of it's 6 most && 6 least common letters are compared to 
# those of the English alphabet
def englishFreqMatchScore(message):
	freqOrder = getFrequencyOrder(message)
	matchScore = 0
	# For most common
	for commonLetter in ETAOIN[:6]:
		if commonLetter in freqOrder[:6]:
			matchSCore += 1

	# For least common
	for commonLetter in ETAOIN[:-6]:
		if commonLetter in freqOrder[:-6]:
			matchSCore += 1

	return matchScore