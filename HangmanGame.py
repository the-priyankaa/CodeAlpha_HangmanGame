#import Library
import random

#lists of words
words = ["game","hangman","play","indoor","won","loss",   "apple", "banana", "orange", "grape", "mango", "peach", "cherry", "lemon", "melon", "papaya",
    "tiger", "lion", "zebra", "rabbit", "monkey", "panda", "koala", "eagle", "falcon", "shark",
    "planet", "galaxy", "comet", "meteor", "rocket", "saturn", "venus", "earth", "orbit", "asteroid",
    "python", "java", "kotlin", "coding", "script", "binary", "server", "client", "kernel", "docker",
    "castle", "village", "bridge", "forest", "desert", "island", "river", "valley", "mountain", "ocean",
    "guitar", "piano", "violin", "trumpet", "drums", "flute", "singer", "melody", "rhythm", "chorus",
    "yellow", "purple", "silver", "golden", "scarlet", "violet", "indigo", "crimson", "turquoise", "amber",
    "winter", "summer", "spring", "autumn", "breeze", "thunder", "rainbow", "sunrise", "sunset", "storm",
    "school", "college", "teacher", "student", "library", "notebook", "pencil", "eraser", "science", "history",
    "coffee", "burger", "pizza", "sandwich", "noodle", "cookie", "carrot", "potato", "tomato", "onion"]

# pick a random word
word = random.choice(words)

# create a list of underscores for the word
display = ["_"] * len(word)

# track wrong guesses
wrong_guesses = 0
max_wrong = 6

# track guessed letters
guessed_letters = set()

#function for hint
def hint():
    # Declare as global
    global wrong_guesses, display, guessed_letters 


#use function for game
def start_game():
    # Declare as global
    global wrong_guesses, display, guessed_letters  

    # Use loop
    while wrong_guesses < max_wrong :

        # Check if player won
        if "_" not in display:
            print(" YOU WON!")
            print(f"The word is {word}") 
            break

        guess = input("Guess a letter: ").lower()

        #check it is an alphabate or not
        if not guess.isalpha():
            print("Invalid input")
            wrong_guesses = wrong_guesses +1
            if wrong_guesses <= 5:
                while True:
                    h=input("Do you want any hint(Y/N):").lower()
                    if h == "y":
                        print()
                        break
                    elif h == "n":
                        ("Play your own!!")
                        break
                    else:
                        print("SORRY! Wrong input!")  

                    continue

        #check it is a repeated guess or not
        if guess in guessed_letters:
            print("OOPS! YOU ALREADY ENTER THIS!")  
            continue

        #check it is a right guess or not
        w = list(word)
        
        if guess in w:
            print("Right guess")

            # Update display with correct letters
            for j in range(len(w)):
                if w[j] == guess:
                    display[j] = guess
                  
        else:
            print("OPPS! WRONG GUESS")
            wrong_guesses = wrong_guesses +1

            if wrong_guesses <= 5:
                while True:
                    h=input("Do you want any hint(Y/N):").lower()
                    if h == "y":
                        print()
                        break
                    elif h == "n":
                        ("Play your own!!")
                        break
                    else:
                        print("SORRY! Wrong input!")
                    continue

        # Add to guessed letters 
        guessed_letters.add(guess) 

        # Check if player lost
        if wrong_guesses == max_wrong:
            print("GAME OVER! You lost!")
            print(f"The word is {word}") 
            continue
       

start_game()
