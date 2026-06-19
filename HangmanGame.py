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
guessed_letters = set()

#use function 
def start_game():
    # Declare as global
    global wrong_guesses, display, guessed_letters  

    # Use loop
    while wrong_guesses < max_wrong:
        guess = input("Guess a letter: ").lower()

        #check it is a right guess or not
        w = list(word)
        
        if guess in w:
            print("Right guess")

            # Update display with correct letters
            for j in range(len(w)):
                if w[j] == guess:
                    display[j] = guess
        elif guess == guessed_letters:
            print("OOPS! YOU ALREADY ENTER THIS!")            
        else:
            print("OPPS! WRONG GUESS")
            wrong_guesses = wrong_guesses +1
        # Add to guessed letters
        guessed_letters.add(guess) 

start_game()
print(word)