# Author: Harrison Toppen-Ryan
# Description : Homework 3, CSCI 141
# Date: October 24th, 2020

# Ensuring a random letter when useing random.choice 
import random 

# First Text and asking player for guess number 
print("Let's play a letter guessing game. The goal for you to guess two letters chosen randomly from among the letters in the word 'bellingham'. The two letters may be the same.")
guess_limit = int(input("How many tries would you like? (enter a number 2-4): "))

# If the guess limit is not in the range required 
if guess_limit < 2 or guess_limit > 4:
    raise SystemExit

# chooses one or two random letters from the word 'bellingham' and defining if a player wins or loeses the game
else:
    guess_count = 0
    out_of_guess = False 
    word = str('bellingham')
    # both letters from the word above choosen randomly 
    letter1 = str(random.choice(word))
    letter2 = str(random.choice(word))
    guess1 = ""
    guess2 = ""
    # when the player wins 
    win = ("You've guessed the secret letters", letter1, "and", letter2, "You win. Woot.")
    # when the player loses 
    loss = ("You are out of tries. Game over. The secret letters were", letter1, "and", letter2)

    # Defining if the number of guesses runs out and how they are counted 
    def noMoreGuesses():
        global guess_count 
        # when the player runs out of guesses 
        if guess_count == guess_limit:
            print(loss)
            raise SystemExit
        # loops back around if the player was wrong 
        else: 
            print("Try", guess_count + 1)
            guess1 = str(input("Guess the first/second letter: "))
            if guess1 == letter1 or letter2:
                print("One of the letters was", guess1)
                guess_count += 1
                noMoreGuesses()
            else: 
                noMoreGuesses()
   
        

    # a while loop seems to be more effective here as the program is told to keep counting as long as the player still has guesses left
    while guess_count < guess_limit and guess1 and guess2 != letter1 or letter2 and not(out_of_guess):
        if guess_count < guess_limit:
            print("Try", guess_count + 1)
            guess1 = input("Guess the first letter: ")
            # if the first guess is the first letter
            if guess1 == letter1:
                print("You've guessed the first letter.")
                guess_count +=1 
                print("Try", guess_count + 1)
                guess2 = input("Guess the second letter: ")
                if guess2 == letter2:
                    # if the player successfully guesses both letters
                    print(win)
                    raise SystemExit
                else:
                    print("The second letter is not", guess2)
                    guess_count +=1
                    noMoreGuesses
            # if the first guess is the second letter 
            elif guess1 == letter2:
                print("You've guessed the second letter.")
                guess_count +=1
                noMoreGuesses()
                print("Try", guess_count + 1) 
                guess1 = str(input("Guess the firstletter: "))
                if guess1 == letter1:
                    print(win)
                    raise SystemExit
                else:
                    print("The first letter is not", guess1)
                    guess_count +=1 
                    noMoreGuesses()
            # if the first or second guess is not the first or second random letter choosen 
            else:
                print("The first letter or second letter is not", guess1)
                guess_count +=1
                print("Try", guess_count + 1)
                guess1 = str(input("Guess the first letter: "))
                if guess1 == letter1:
                    print("You've guessed the first letter.")
                    guess_count += 1
                    noMoreGuesses()
                else:
                    print("The first letter or second letter is not", guess1)
                    guess_count +=1
                    noMoreGuesses()
                    

        else: 
            # if the players were out of guesses 
            out_of_guess = True
 
    if out_of_guess:
        print(loss)
   
    

    

