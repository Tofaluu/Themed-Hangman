import words
import hangman

removedWords = []
winterWords = words.winter_words
schoolWords = words.school_words
movieWords = words.movie_words
foodWords = words.food_words
placeWords = words.place_words
companyWords = words.company_words

winterHangman = hangman.winterHangman
schoolHangman = hangman.schoolHangman
movieHangman = hangman.movieHangman
foodHangman = hangman.foodHangman
placeHangman = hangman.placeHangman
companyHangman = hangman.companyHangman

b = ""
c = ""
x = ""
currentHangman = ""

letterIndex = 0
points = 0
hangmanIndex = 0
highScore = 0