import random
import requests

def chooseAWord():
	wordSite = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
	response = requests.get(wordSite)
	wordDictionary = response.content.splitlines()
	#wordDictionary = ['sun', 'moon', 'earth', 'jupiter', 'mercury', 'neptune', 'mars']
	print("Work dictionary: ", wordDictionary[1].decode('UTF-8'), len(wordDictionary[1]))

	chosenWord = random.choice(wordDictionary).decode('UTF-8')
	#chosenWord = wordDictionary[random.randrange(0, len(wordDictionary), 1)]
	print("Word randomly generated for the game...!")
	print("Word to guess is: ", chosenWord)
	printChosenWord(chosenWord)

	chosenWordList = list(chosenWord)
	print(chosenWordList)

def printChosenWord(chosenWord):
	for letter in chosenWord:
		print("- "),

def initializeGuessedWord():
	guessedWordList = ["_"] * len(chosenWord)
print("guessed word is",guessedWordList)

print("Welcome to Hangman game!!!")

maxAttempts = 0
numOfAttempts = 0
answer = False
for i in range(0,len(chosenWordList)):
	print (i, chosenWord[i])
print("You will have total " + str(maxAttempts) + " attempts to correctly guess the word.")

chooseAWord()

while (numOfAttempts <= maxAttempts):
	guessed = False
	inputLetter = input("Input a letter: ")
	if (inputLetter in guessedWordList):
		print("You have already chosen this letter. Choose a different one")
		continue
	for i in range(0,len(chosenWordList)):
		if (chosenWordList[i] == inputLetter):
			guessedWordList[i] = inputLetter
			guessed = True
	if (chosenWordList == guessedWordList):
		answer = True
		break
	if (not guessed):
		numOfAttempts += 1

print("Chosen word was:", chosenWord)
print("You guessed:    ", ''.join(map(str, guessedWordList)))

if (answer):
	print("Congratulations! You guessed the word correctly.")
else:
	print("You exceeded number of attempts. Better luck next time!")

# keep guessed string guessedWord
# cannot guess same letter again

# end of file
