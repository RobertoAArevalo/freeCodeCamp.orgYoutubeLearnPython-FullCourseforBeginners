#Lesson 19 - Building a Guessing Game

#there will be a secrete word stored inside of the program and a user will
# interact with the program and try to guess it. We want the user to keep guessing
# what the secret word will be.

# First thing will be creating a variable to store the secret word.
# Second, create a variable that will store the users responses.
# We will use a while loop to continually ask the user to continually guess the wrod until it is guessed.
# Create a looping guard.
# There can be a limit set. There will need to be more variables set.

secret_word = "giraffe" #variable
guess = "" #variable
guess_count = 0 #variable, keeps track of how many times the user has guessed the word
guess_limit = 3 #will tell us how many times the user can guess the limit
out_of_guesses = False #bullion that will tell us if the user is out of guesses. If it is true, than they lost the game.


#one more condition is and not will allow for code to keep running
while guess != secret_word and not (out_of_guesses): #stored word will check on while guess, if it isn't than it reruns.
    if guess_count < guess_limit: #If true they still have guesses left, and will be allowed to guess again. If not, they lose.
    # If the secret word is guessed and loop is broken.
    #store
        guess = input("Enter guess: ") #response
        guess_count += 1 #This will keep track of guesses by incrementing the guess count.
    else:
        out_of_guesses = True

if out_of_guesses: # Is used to determine which scenario to run based on winning or not.
    print("Out of Guesses, YOU LOSE!")
else: # To determine that they won.
    print("You win!")

"""
returns 
Enter guess: a
Enter guess: a
Enter guess: giraffe
You win!

Process finished with exit code 0
"""
