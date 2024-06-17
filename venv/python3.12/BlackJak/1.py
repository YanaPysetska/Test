import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    '''функцыя возвращает рандомную
    карту из списка - cards'''
    return random.choice(cards)

user_cards = []
computer_cards = []

def calculate_score(List_of_cards):
    if sum(List_of_cards)==21 and len(List_of_cards)==2:
        return 0
    if 11 in List_of_cards and sum(List_of_cards)>21:
        List_of_cards.remove(11)
        List_of_cards.append(1)
    return sum(List_of_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score == 0:
        return "User wins with a Blackjack!"
    elif user_score > 21:
        return "User busts. Computer wins!"
    elif computer_score > 21:
        return "Computer busts. User wins!"
    elif user_score > computer_score:
        return "User wins!"
    else:
        return "Computer wins!"


def game():
    print(logo)
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_input = input("Do you want to draw another card? (yes/no): ").strip().lower()
            if user_input == 'yes':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while True:
    game()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Bye.")
        break

