import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_integer = random.randint(1, 100)
print(f"Pssst, the correct answer is {random_integer}")

def game(lvl):
    user_guess=0
    while user_guess!=random_integer and lvl>0:
        print(f"You have {lvl} attempts remaining to guess the number.")
        lvl-=1
        user_guess=int(input("Make a guess: "))
        if user_guess==random_integer:
            print(f"You got it! The answer was {random_integer}.")
        elif lvl==0:
            print("You've run out of guesses, you lose.")
        elif user_guess>random_integer:
            print("Too high. \nGuess again.")
        elif user_guess<random_integer:
            print("Too low. \nGuess again.")
        else:
            print("Guess again.")

user_input_lvl=input("Choose a difficulty. Type 'easy' or 'hard':")
if user_input_lvl=="easy":
     game(10)
else:
     game(5)
