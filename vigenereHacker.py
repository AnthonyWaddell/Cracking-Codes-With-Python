'''Vigenere cipher hacker. Slightly more sophisticated than a dictionary attack. 
	Will work with randomly generated string keys.'''

'''import itertools
import re
import pyperclip
import vigenereCipher
import freqAnalysis
import detectEnglish'''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Will not attempt keys longer than this.
MAX_KEY_LENGTH = 16
# Attempt this many letters per subkey.
NUM_MOST_FREQ_LETTERS = 4
# If set to True, program doesn't print anything
SILENT_MODE = False
NONLETTERS_PATTERN = re.compile('[^A-Z]')

def main():
	ciphertext = """Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, 
	kdmktsvmztsl, izr xoexghzr kkusitaaf. Vz wsa twbhdg ubalmmzhdad qz hce 
	vmhsgohuqbo ox kaakulmd gxiwvos, krgdurdny i rcmmstugvtawz ca tzm ocicwxfg 
	jf "stscmilpy" oid "uwydptsbuci" wabt hce Lcdwig eiovdnw. Bgfdny qe kddwtk 
	qjnkqpsmev ba pz tzm roohwz at xoexghzr kkusicw izr vrlqrwxist uboedtuuznum. 
	Pimifo Icmlv Emf DI, Lcdwig owdyzd xwd hce Ywhsmnemzh Xovm mby Cqxtsm Supacg 
	(GUKE) oo Bdmfqclwg Bomk, Tzuhvif'a ocyetzqofifo ositjm. Rcm a lqys ce oie 
	vzav wr Vpt 8, lpq gzclqab mekxabnittq tjr Ymdavn fihog cjgbhvnstkgds. Zm 
	psqikmp o iuejqf jf lmoviiicqg aoj jdsvkavs Uzreiz qdpzmdg, dnutgrdny bts 
	helpar jf lpq pjmtm, mb zlwkffjmwktoiiuix avczqzs ohsb ocplv nuby swbfwigk 
	naf ohw Mzwbms umqcifm. Mtoej bts raj pq kjrcmp oo tzm Zooigvmz Khqauqvl 
	Dincmalwdm, rhwzq vz cjmmhzd gvq ca tzm rwmsl lqgdgfa rcm a kbafzd-hzaumae 
	kaakulmd, hce SKQ. Wi 1948 Tmzubb jgqzsy Msf Zsrmsv'e Qjmhcfwig Dincmalwdm 
	vt Eizqcekbqf Pnadqfnilg, ivzrw pq onsaafsy if bts yenmxckmwvf ca tzm 
	Yoiczmehzr uwydptwze oid tmoohe avfsmekbqr dn eifvzmsbuqvl tqazjgq. Pq 
	kmolm m dvpwz ab ohw ktshiuix pvsaa at hojxtcbefmewn, afl bfzdakfsy 
	okkuzgalqzu xhwuuqvl jmmqoigve gpcz ie hce Tmxcpsgd-Lvvbgbubnkq zqoxtawz, 
	kciup isme xqdgo otaqfqev qz hce 1960k. Bgfdny'a tchokmjivlabk fzsmtfsy if 
	i ofdmavmz krgaqqptawz wi 1952, wzmz vjmgaqlpad iohn wwzq goidt uzgeyix wi 
	tzm Gbdtwl Wwigvwy. Vz aukqdoev bdsvtemzh rilp rshadm tcmmgvqg (xhwuuqvl 
	uiehmalqab) vs sv mzoejvmhdvw ba dmikwz. Hpravs rdev qz 1954, xpsl whsm tow 
	iszkk jqtjrw pug 42id tqdhcdsg, rfjm ugmbddw xawnofqzu. Vn avcizsl lqhzreqzsy 
	tzif vds vmmhc wsa eidcalq; vds ewfvzr svp gjmw wfvzrk jqzdenmp vds vmmhc wsa 
	mqxivmzhvl. Gv 10 Esktwunsm 2009, fgtxcrifo mb Dnlmdbzt uiydviyv, Nfdtaat 
	Dmiem Ywiikbqf Bojlab Wrgez avdw iz cafakuog pmjxwx ahwxcby gv nscadn at ohw 
	Jdwoikp scqejvysit xwd "hce sxboglavs kvy zm ion tjmmhzd." Sa at Haq 2012 i 
	bfdvsbq azmtmd'g widt ion bwnafz tzm Tcpsw wr Zjrva ivdcz eaigd yzmbo Tmzubb 
	a kbmhptgzk dvrvwz wa efiohzd."""

	hackedMessage = hackVigenere(ciphertext)

	if hackedMessage != None:
		print('Copying hacked message to clipboard...')
		print(hackedMessage)
		pyperclip.copy(hackedMessage)
	else:
		print('Failed to break encryption...')

def findRepeatSequenceSpacings(message):
	# Run through message looking for repeated 3-5 letter sequences
	message = NONLETTERS_PATTERN.sub('', message.upper())
	# Compile a list of seqLen-letter sequences found in the message
	# keys = sequences, values = list of in spacings
	seqSpacings = {} 
	for seqLen in range(3, 6):
		for seqStart in range(len(message) - seqLen):
			# Determine what the sequence is and store it in seq
			seq = message[seqStart:seqStart + seqLen]

			# Now look for this sequence in the rest of the message
			for i in range(seqStart + seqLen, len(message) - seqLen):
				if message[i:i + seqLen] == seq:
					# Repeated sequence has been located
					if seq not in seqSpacings:
						seqSpacings[seq] = []

					# Append the spacing distance between the repeated sequence and original sequence
					seqSpacings[seq].append(i - seqStart)
	return seqSpacings

def getUsefulFactors(num):
	# Returns a list of useful factors of parameter. Useful = less
	# than the max key length  + 1 and not 1. eg for num = 144
	# returns [2, 3, 4, 6, 8, 9, 12, 16]

	if num < 2:
		return []

	factors = []
	# Only look for factors up to the max key length (16)
	for i in range(2, MAX_KEY_LENGTH + 1):
		if num % i == 0:
			factors.append(i)
			otherFactor = int(num / i)
			if otherFactor < MAX_KEY_LENGTH + 1 and otherFactor != 1:
				factors.append(otherFactor)

	return list(set(factors))

def getItemAtIndexOne(x):
	return x[1]

def getMostCommonFactors(seqFactors):
	# First, get a count of how many times a factor occurs in seqFactors
	factorCounts = {}

	# seqFactors keys are sequences. values are lists of factors of the spacings
	for seq in seqFactors:
		factorList = seqFactors[seq]
		for factor in factorList:
			if factor not in factorCounts:
				factorCounts[factor] = 0
			factorCounts[factor] += 1

	# Now put the factor count in a tuple, make them into a list, and sort them
	factorsByCount = []
	for factor in factorCounts:
		if factor <= MAX_KEY_LENGTH:
			factorsByCount.append((factor, factorCounts[factor]))
	factorsByCount.sort(key = getItemAtIndexOne, reverse = True)

	return factorsByCount

def kasiskiExamination(ciphertext):
	# Find sequences of 3 to 5 chars that appear multiple times
	repeatedSeqSpacings = findRepeatSequenceSpacings(ciphertext)

	seqFactors = {}
	for seq in repeatedSeqSpacings:
		seqFactors[seq] = []
		for spacing in repeatedSeqSpacings[seq]:
			seqFactors[seq].extend(getUsefulFactors(seqFactors))

	factorsByCount = getMostCommonFactors(seqFactors)

	# Now take factors from factorsByCount and put them in a list to use later
	allLikelyKeyLengths = []
	for twoIntTuple in factorsByCount:
		allLikelyKeyLengths.append(twoIntTuple[0])

	return allLikelyKeyLengths

def getNthSubkeysLetters(nth, keyLength, message):
''' Return every nth letter for each keyLength set of letters in text
	eg: getNthSubkeysLetters(1, 3, 'ABCABCABC') RETURN 'AAA' 
	eg: getNthSubkeysLetters(2, 3, 'ABCABCABC') RETURN 'BBB' 
	eg: getNthSubkeysLetters(3, 3, 'ABCABCABC') RETURN 'CCC' 
	eg: getNthSubkeysLetters(1, 5, 'ABCDEFGHI') RETURN 'AF'''
	MESSAGE = NONLETTERS_PATTERN.sub('', message)

	i = nth - 1
	letters = []
	while i < len(message):
		letters.append(message[i])
		i += keyLength
	return ''.join(letters)	

def attemptHackWithKeyLength(ciphertext, mostLikelyKeyLength):
	# Determine the most likely letters for each letter in the key:
	ciphertextUp = ciphertext.upper()
	# allFreqScores is a ilst of mostLikelyKeyLength numbers of lists
	# These inner lists are the freqScores lists
	allFreqScores = []
	for nth in range(1, mostLikelyKeyLength + 1):
		nthLetters = getNthSubkeysLetters(nth, mostLikelyKeyLength, ciphertextUp)

		# freqScores is a list of tuples like:
		# [(<letter>, <Eng. Freq. match score>), ... ]
		# List is sorted =by match score, higher score = better match
		freqScores = []
		for possibleKey in LETTERS:
			decryptedText = vigenereCipher.decryptMessage(possibleKey, nthLetters)
			keyAndFreqMatchTuple = (possibleKey, freqAnalysis.englishFreqMatchScore(decryptedText))
			freqScores.append(keyAndFreqMatchTuple)
		# Sort by match score
		freqScores.sort(key = getItemAtIndexOne, reverse = True)

		allFreqScores.append(freqScores[:NUM_MOST_FREQ_LETTERS])

    if not SILENT_MODE:
        for i in range(len(allFreqScores)):
        	# Use i + 1 so the first letter is not called the "0th" letter
        	print('Possible letters for letter %s of the key: ' % (i + 1), end = '')
        	for freqScore in allFreqScores[i]:
        		print('%s' % freqScore[0], end = '')
    		print()

	# Try every combo of the most likely letters for each position in the key
	for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat = mostLikelyKeyLength):
		# Creat a possible key from the letters in allFreqScores
		possibleKey = ''
		for i in range(mostLikelyKeyLength):
			possibleKey += allFreqScores[i][index[i][0]]

		if not SILENT_MODE:
			print('Attempting with key: %s' % (possibleKey))

		decryptedText = vigenereCipher.decryptMessage(possibleKey, ciphertextUp)

		if detectEnglish.isEnglish(decryptedText):
			# Set the hacked ciphertext to the original casing
			origCase = []
			for i in range(len(ciphertext)):
				if ciphertext[i].isupper():
					origCase.append(decryptedText[i].upper())
				else:
					origCase = ''.join(origCase)

			# Check with user
			print('Possible encryption hack with key %s: ' % (possibleKey))
			print(decryptedText[:200])
			print()
			print('Enter D if done, or anything else to continue hacking...')
			response = input('>')

			if response.strip().upper().startswith('D'):
				return decryptedText
	# If no English looking word is found
	return None

def hackVigener(ciphertext):
	# First do a Kasiski Examination to figure out what the length of the 
	# ciphertexts encryption key is
	allLikelyKeyLengths = kasiskiExamination(ciphertext)
	if not SILENT_MODE:
		keyLengthStr = ''
		for keyLength in allLikelyKeyLengths:
			keyLengthStr += '%s ' % (keyLength)
		print('Kasiski Examination results say the most likely key length are: ' + keyLengthStr + '\n')
	hackedMessage = None
	for keyLength in allLikelyKeyLengths:
		if not SILENT_MODE:
			print('Attempting to hack with key length %s (%s possible keys)...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
		hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
		if hackedMessage != None:
			break

	# If none of the key length found by Kasiski examination worked, start bruteforcing
	if hackedMessage == None:
		if not SILENT_MODE:
			print('Unable to hack message with likelye key length(S). Brute forcing key length...')
		for keyLength in range(1, MAX_KEY_LENGTH + 1):
			# Don't re-check key lengths already tried from Kasiski
			if keyLength not in allLikelyKeyLengths:
				if not SILENT_MODE:
					print(' Attempting to hack with key length %s (%s possible keys...' % (keyLength, NUM_MOST_FREQ_LETTERS ** keyLength))
				hackedMessage = attemptHackWithKeyLength(ciphertext, keyLength)
				if hackedMessage != None:
					break
	return hackedMessage

# If ran instead of imported
if __name__ == '__main__':
	main()