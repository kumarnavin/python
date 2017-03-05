import random
import requests
import sys

def chooseAWord():
	wordSite = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	response = requests.get(wordSite)
	wordDictionary = response.content.decode('UTF-8').splitlines()
	print(wordDictionary)

	chosenWord = random.choice(wordDictionary).upper()
	#print("Word randomly generated for the game is:", chosenWord)
	return chosenWord

def initializeGuessedWord(lenWord):
	guessedLetters = ["_"] * lenWord
	return guessedLetters

def printWordFormatted(letters, doMask=False):
	print("********************************")
	sys.stdout.write("Chosen word: " if doMask else "Guessed word: ")
	for letter in letters:
		#print("letter:", letter)
		sys.stdout.write('X' if doMask else letter)


###########################
### GAME STARTS HERE ######
###########################

print("Welcome to Hangman game!!!")

maxAttempts = 6
numOfAttempts = 0
answer = False
print("You will have total " + str(maxAttempts) + " attempts to correctly guess the word.")

chosenWord = chooseAWord()
chosenLetters = list(chosenWord)
lenChosenWord = len(chosenWord)
printWordFormatted(chosenLetters, True)
print("\n")

guessedLetters = initializeGuessedWord(lenChosenWord)
printWordFormatted(guessedLetters)

guessList = []

while (numOfAttempts < maxAttempts):
	guessed = False
	inputLetter = input("\nInput a letter: ").upper()
	if (inputLetter in guessedLetters):
		print("You have already chosen this letter. Choose a different one")
		continue
	guessList.append(inputLetter)
	for i in range(0,lenChosenWord):
		# if letter not guessed yet, see it exists in chosen word
		if (guessedLetters[i] == '_' and chosenLetters[i] == inputLetter):
			guessedLetters[i] = inputLetter
			guessed = True
	if (chosenLetters == guessedLetters):
		answer = True
		break
	if (not guessed):
		numOfAttempts += 1
	printWordFormatted(guessedLetters)
	print("\nAttempts remaining: ", (maxAttempts - numOfAttempts))
	print("Guessed letters so far", guessList)

print("********************************")
print("Chosen word was:", chosenWord)
print("You guessed:    ", ''.join(map(str, guessedLetters)))
print("********************************")

if (answer):
	print("Congratulations! You guessed the word correctly.")
else:
	print("You exceeded number of attempts. Better luck next time!")

# keep guessed string guessedWord
# cannot guess same letter again

# end of file
