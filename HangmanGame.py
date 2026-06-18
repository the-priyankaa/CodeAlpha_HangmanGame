#import Library
import random

#lists of words
words = ["game","hangman","play","indoor","won","loss"]

# pick a random word
word = random.choice(words)

# create a list of underscores for the word
display = ["_"] * len(word)

# track wrong guesses
wrong_guesses = 0
max_wrong = 6

# track guessed letters
guessed_letters = []


