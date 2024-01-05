import functions
from variables import removedWords
valid = False
while not valid: # Checks whether the theme is valid, and if not, it'll ask again until it is valid
  theme = input("What theme do you want to play? (Winter, School, Movie, Food, Place, Company):\n\n").lower()
  if theme in ["winter", "school", "movie", "food", "place", "company"]:
    valid = True
  else:
    print("\nInvalid input, try again.\n")

themeWords = functions.wordList(theme) # stores the list of words in the variable
word = functions.wordAdd(themeWords) # records the randomly chosen word from the list
functions.wordRemove(themeWords, word) # removes the word from the list
hangman = functions.wordHangman(theme) # stores the hangman list 
removedWords.append(word) # adds the chosen word to the removed words list


from variables import b, c, x, currentHangman # Adds the empty string variables used for the word outputs

for i in word: # outputs the word, but replaced by underscores
  if i == " ":
    outputWord = " "
  else:
    outputWord = i.replace(i, "_")
  print(outputWord, end = " ")
  x += outputWord # The word replaced by underscores (not including the extra spaces)
for a in word:
  b += a
  b += " "
y = b # the original word is stored into y (including the extra spaces between words)

from variables import letterIndex, points, hangmanIndex, highScore # Adds the variables used to record score and keep track of the index positions

while True:
  valid = False
  while not valid:
    userGuess = input("\n\nWhat letter would you like to guess?\n\n").lower()
    if userGuess.isalpha() == False:
      print("\nInvalid guess, try again")
    else:
      valid = True

  print("\n")

  if not userGuess in word.lower(): # prints a part of the hangman if the guess is wrong
    currentHangman += hangman[hangmanIndex]
    print(f"\n{currentHangman}\n")
    hangmanIndex += 1 # Adds the next part of the hangman

  for i in word: # Checks through the word to see if and where the guessed letter appears
    if i.lower() == " ":
      outputWord = " "
    elif x[letterIndex].isalpha():
      outputWord = i 
    elif userGuess == i.lower():
      outputWord = i.replace(i, userGuess)
    else:
      outputWord = "_"
    print(outputWord, end = " ")
    letterIndex += 1
    x += outputWord 
    c += outputWord
    c += " " # Makes a copy of the current output
  if y.lower() in c.lower():
    points += 1

    if points == 20: # If all words are completed
      print(f"\n\nWait...What??? You completed all 20 {theme.capitalize()} words! You didn't cheat, did you? Well, you beat the game, so good job and thanks for playing :)")
      break

    print(f"\n\nYou have {points} point(s) right now. Moving on to the next word:\n\n")

    word = functions.wordAdd(themeWords)
    functions.wordRemove(themeWords, word)
    removedWords.append(word)

    from variables import b, c, x

    for i in word:
      if i == " ":
        outputWord = " "
      else:
        outputWord = i.replace(i, "_")
      print(outputWord, end = " ")
      x += outputWord
    for a in word:
      b += a
      b += " "
    y = b

    from variables import letterIndex # resets letter index

  if hangmanIndex == 10: # Checks whether the game is over
    if points > highScore:
      highScore = points
    print(f"\n\nGame over! You got {points} point(s)\n\nHigh Score: {highScore}")

    valid = False
    while not valid:
      playAgain = input("\nWould you like to play again? (yes or no): ").lower()
      if playAgain in ["yes", "no"]:
        valid = True
      else:
        print("\nInvalid input, try again.\n")


    if playAgain in "no":
      print("\nThanks for playing!")
      break

    elif playAgain in "yes": # If yes, repeats the beginning process
      themeWords.extend(removedWords)
      removedWords = []

      valid = False
      while not valid: 
        theme = input("\nWhat theme do you want to play? (Winter, School, Movie, Food, Place, Company):\n\n").lower()
        if theme in ["winter", "school", "movie", "food", "place", "company"]:
          valid = True
        else:
          print("\nInvalid input, try again.\n")

      themeWords = functions.wordList(theme)
      word = functions.wordAdd(themeWords)
      functions.wordRemove(themeWords, word)
      hangman = functions.wordHangman(theme)
      removedWords.append(word)

      from variables import b, c, x, currentHangman

      for i in word:
        if i == " ":
          outputWord = " "
        else:
          outputWord = i.replace(i, "_")
        print(outputWord, end = " ")
        x += outputWord
      for a in word:
        b += a
        b += " "
      y = b

      from variables import letterIndex, points, hangmanIndex # resets the indexes and points back to 0