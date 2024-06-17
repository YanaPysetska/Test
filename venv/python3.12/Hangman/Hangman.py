import random
from hangman_art import stages
from hangman_words import word_list
from hangman_art import logo
chosen_word = random.choice(word_list)
lives = 6
print(logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # Track if the guess was correct
    if guess in display:
        print(f"you entered a letter that already guessed {guess}")

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    # If the guess was incorrect, reduce lives
    if guess not in chosen_word:
        lives -= 1
        if lives >= 0:
            print(stages[lives])
        elif lives==-2:
            print(stages[-2])
        print(f"Incorrect guess {guess}. You have {lives} lives left.")
        if lives == 0:
            print("You lose.")
            break

    print(display)

if "_" not in display:
    print("You win!")
