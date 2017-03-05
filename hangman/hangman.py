# Author: Navin Kumar

import random
import requests
import sys


# This function invokes a REST API call to get a list of words.
# A random word is then picked up for the game.
def chooseAWord(mode="ADULT"):
	wordSite = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	response = requests.get(wordSite)
	wordDictionary = response.content.decode('UTF-8').splitlines()
	print(wordDictionary)

	# Kid mode gets words with 4 or less characters :)
	if (mode == "KID"):
		wordDictionary = [word for word in wordDictionary if len(word) in range(3, 4)]
	word = random.choice(wordDictionary).upper()
	# print("Word randomly generated for the game is:", chosenWord)
	return word


# This function initializes player's guessed word with underscores.
def initializeGuessedWord(lenWord):
	guessedLetters = ["_"] * lenWord
	return guessedLetters


# This function prints the word.
# optional boolean doMask is passed as True for chosen word so we don't display actual word.
# sys.stdout.write is used to print the letters on the same line without newline break.
def printWordFormatted(letters, doMask=False):
	print("********************************")
	sys.stdout.write("Chosen word: " if doMask else "Guessed word: ")
	for letter in letters:
		# print("letter:", letter)
		sys.stdout.write('X' if doMask else letter)


# **************** #
# GAME STARTS HERE #
# **************** #

print("Welcome to Hangman game!!!")

mode = input("Pick the mode (kid or adult): ").upper()

# Initialize variables
maxAttempts = 6
numOfAttempts = 0
answered = False
print("You will have total " + str(maxAttempts) + " attempts to correctly guess the word.")

# Choose a word
chosenWord = chooseAWord(mode)
chosenLetters = list(chosenWord)
lenChosenWord = len(chosenWord)
printWordFormatted(chosenLetters, True)
print("\n")

# Initialize guessed word
guessedLetters = initializeGuessedWord(lenChosenWord)
printWordFormatted(guessedLetters)

# Maintain the list of all guessed letters (matched or unmatched)
guessList = []

# Loop while player has some attempts remaining
while (numOfAttempts < maxAttempts and
		   not answered):
	correctGuess = False
	inputLetter = input("\nInput a letter: ").upper()
	if (inputLetter in guessList):
		print("You have already chosen this letter. Choose a different one")
		continue
	guessList.append(inputLetter)
	for i in range(0, lenChosenWord):
		# if letter not guessed yet, see it exists in chosen word
		if (guessedLetters[i] == '_' and
					chosenLetters[i] == inputLetter):
			guessedLetters[i] = inputLetter
			correctGuess = True
	answered = (chosenLetters == guessedLetters)
	if not correctGuess:
		numOfAttempts += 1
	printWordFormatted(guessedLetters)
	print("\nAttempts remaining: ", (maxAttempts - numOfAttempts))
	print("Guessed letters so far", guessList)

print("********************************")
print("Chosen word was:", chosenWord)
print("You guessed:    ", ''.join(map(str, guessedLetters)))
print("********************************")

if answered:
	print("Congratulations! You guessed the word correctly.")
else:
	print("You exceeded number of attempts. Better luck next time!")


# end of file