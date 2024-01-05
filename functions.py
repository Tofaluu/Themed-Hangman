from variables import winterHangman, schoolHangman, movieHangman, foodHangman, placeHangman, companyHangman

import random
import words

def wordAdd(themeWords):
  return random.choice(themeWords)

def wordRemove(themeWords, word):
  themeWords.remove(word)

def wordHangman(theme):
  if theme == "winter":
    return winterHangman
  elif theme == "school":
    return schoolHangman
  elif theme == "movie":
    return movieHangman
  elif theme == "food":
    return foodHangman
  elif theme == "place":
    return placeHangman
  elif theme == "company":
    return companyHangman

def wordList(theme):
  if theme == "winter":
    return words.winter_words
  elif theme == "school":
    return words.school_words
  elif theme == "movie":
    return words.movie_words
  elif theme == "food":
    return words.food_words
  elif theme == "place":
    return words.place_words
  elif theme == "company":
    return words.company_words