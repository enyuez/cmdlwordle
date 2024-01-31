################################################################################
# Select random word from word list
################################################################################

import random


def get_word():
  '''
  Returns a random word from the word list
  '''
  with open("sgb-words.txt", "r") as f:
    words = f.readlines()
  return random.choice(words)[:-1]
