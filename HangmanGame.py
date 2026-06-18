#import Library
import random

#lists of words
words = ["game","hangman","play","indoor","won","loss"]

# Pick a random word
word = random.choice(words)

#Create a list of underscores for the word
display = ["_"] * len(word)

