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
    if mode == "KID":
        wordDictionary = [word for word in wordDictionary if len(word) in range(3, 4)]
    word = random.choice(wordDictionary).upper()
    # print("Word randomly generated for the game is:", chosenWord)
    return word


# This function initializes player's guessed word with underscores.
def initializeGuessedWord(lenWord):
    guessedLetters = ["_"] * lenWord
    return guessedLetters


# Pick up a new letter (not already guessed before)
def pickALetter(alreadyGuessed):
    isAlreadyPicked = True
    inputLetter = ""
    while isAlreadyPicked:
        inputLetter = input("\nInput a letter: ").upper()
        if (inputLetter in alreadyGuessed):
            print("You already chose this letter. Choose a different one")
        else:
            isAlreadyPicked = False
    return inputLetter


# This function prints the word.
# 1. Optional boolean doMask is passed as True for chosen word
# so that we ask actual word with XXX... while displaying.
# 2. sys.stdout.write prints letters on the same line without newline break.
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

continuePlaying = True
while continuePlaying:
    mode = input("Pick the mode (kid or adult): ").upper()

    # Initialize variables
    MAX_ATTEMPTS = 6
    numOfAttempts = 0
    isAnswered = False
    print("You will have total " + str(MAX_ATTEMPTS) + " attempts to correctly guess the word.")

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
    alreadyGuessed = []

    # Loop while player has some attempts remaining
    while numOfAttempts < MAX_ATTEMPTS and \
            not isAnswered:
        correctGuess = False
        inputLetter = pickALetter(alreadyGuessed)
        alreadyGuessed.append(inputLetter)
        for i in range(0, lenChosenWord):
            # if letter not guessed yet, see it exists in chosen word
            if (guessedLetters[i] == '_' and
                    chosenLetters[i] == inputLetter):
                guessedLetters[i] = inputLetter
                correctGuess = True
            isAnswered = (chosenLetters == guessedLetters)
        if not correctGuess:
            numOfAttempts += 1
        printWordFormatted(guessedLetters)
        print("\nAttempts remaining: ", (MAX_ATTEMPTS - numOfAttempts))
        print("Guessed letters so far", alreadyGuessed)

    print("********************************")
    print("Chosen word was:", chosenWord)
    print("You guessed:    ", ''.join(map(str, guessedLetters)))
    print("********************************")

    if isAnswered:
        print("Congratulations! You guessed the word correctly.")
    else:
        print("You exceeded number of attempts. Better luck next time!")
    continueYN = input("Do you want to continue playing (y/n)?").upper()
    continuePlaying = True if continueYN == "Y" else False
# End of file
