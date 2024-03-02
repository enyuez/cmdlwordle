################################################################################
# Python program building command line Wordle game!
#
# Game rules adapted from New York Times
#   https://www.nytimes.com/2023/08/01/crosswords/how-to-talk-about-wordle.html
#
# Words sourced from Stanford GraphBase
#   https://www-cs-faculty.stanford.edu/~knuth/sgb.html
################################################################################

from termcolor import colored
from word import get_word

WELCOME_MESSAGE = "Welcome to CommandLine Wordle!"
OPTIONS = [
  "s : start new game", "q : quit", "i : show instructions", "c : show answer"
]
INSTRUCTIONS = [
  "1. You have 6 guesses to find the secret 5-letter word.",
  "2. Each guess must be a valid five-letter word - a Valid Word is a 5 letter word found in our game dictionary (sgb-words.txt)",
  "3. The color of a letter will change to show you how close your guess was",
  "4. If the letter turns green, the letter is in the word, and it is in the correct spot",
  "5. If the letter turns yellow, the letter is in the word, but it is not in the correct spot",
  "6. If the letter turns red, the letter is not in the word"
]


def start_game(SECRET_WORD):
  print("\nGame started!\n  You have 6 guesses remaining!\n")
  gr = 6

  while (gr > 0):
    user_g = input("Please input your guess: ").casefold()
    # Check that guess is valid word 
    if len(user_g) != 5:
      print(
        f"You guessed {user_g}; this is invalid because it is not 5 characters long. Please try again. You have {gr} guesses remaining."
      )
      continue
    elif user_g == SECRET_WORD:
      print(colored(SECRET_WORD, 'green'))
      print("You win!")
      return
    else:
      res = check_guess(SECRET_WORD, user_g)
      ps = ""
      for i in range(5):
        if res[i] == "W":
          ps += colored(user_g[i], 'yellow')
        elif res[i] == "C":
          ps += colored(user_g[i], 'green')
        else:
          ps += colored(user_g[i], 'grey')
      print(ps)
      gr -= 1
  if (gr == 0):
    print("Out of guesses! You lose!\n\n")


def check_guess(word, guess):
  s = ""
  lw = list(word)
  lg = list(guess)
  wp = []
  for i in range(5):
    if lg[i] == lw[i]:
      s += "C"
      lw[i] = "-"
    elif lg[i] in lw:
      s += "*"
      wp.append(lg[i])
    else:
      s += "N"
  ls = list(s)
  for letter in wp:
    if letter in lw:
      for i in range(len(ls)):
        if ls[i] == "*":
          ls[i] = "W"
          break
    else:
      for i in range(len(ls)):
        if ls[i] == "*":
          ls[i] = "N"
          break
  return "".join(ls)


if __name__ == "__main__":
  print(WELCOME_MESSAGE)
  SECRET_WORD = get_word()

  while (1):
    print("\nPick one of 4 game modes:\n")
    for option in OPTIONS:
      print(option)
    option = input("\nPlease select an option: ")
    if option == "s":
      start_game(SECRET_WORD)
      SECRET_WORD = get_word()
    elif option == "i":
      print("\nWelcome to CommandLine Wordle! Here are the rules:\n")
      for instruction in INSTRUCTIONS:
        print(instruction)
    elif option == "c":
      print(f"The answer is {colored(SECRET_WORD, 'green')}")
    elif option == "q":
      exit(1)
    else:
      print("Invalid option. Please try again.")
