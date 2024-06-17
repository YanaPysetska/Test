from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)
current_score=0
current_winner = random.choice(data)

while True:
    remaining_data = []
    for i in data:
        if i != current_winner:
            remaining_data.append(i)

    random_opponent = random.choice(remaining_data)

    print(f"Compare A: {current_winner['name']}, a {current_winner['description']} from {current_winner['country']} => {current_winner['follower_count']}")
    print(vs)
    print(f"Against B: {random_opponent['name']}, a {random_opponent['description']} from {random_opponent['country']} =>{random_opponent['follower_count']}")

    user_choise=input("Who has more followers? Type 'A' or 'B':").lower()

    clear()
    print(logo)
    if user_choise=='a' and current_winner['follower_count']>random_opponent['follower_count']:
        current_score+=1
        print(f"You're right! Current score: {current_score}.")
    elif user_choise=='b' and random_opponent['follower_count']>current_winner['follower_count']:
        current_score+=1
        print(f"You're right! Current score: {current_score}.")
        current_winner = random_opponent
    else:
        print(f"Sorry, that's wrong. Final score: {current_score}")
        break
