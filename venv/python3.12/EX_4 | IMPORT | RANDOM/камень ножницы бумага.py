rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


import random
human_choise=input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.')
if human_choise == '0':
    print(rock)
elif human_choise == '1':
    print(paper)
elif human_choise == '2':
    print(scissors)
else:
    print('invalid number')

options = [rock, scissors, scissors]
computer_option = random.choice(options)
print(f'Computer chose:{computer_option}')

if human_choise == '0' and computer_option == scissors:
  print('You win')
elif human_choise == '1' and computer_option == rock:
    print('You win')
elif human_choise == '2' and computer_option == paper:
    print('You win')
elif human_choise == '0' and computer_option == rock:
    print('Draw')
elif human_choise == '1' and computer_option == paper:
    print('Draw')
elif human_choise == '2' and computer_option == scissors:
    print('Draw')
else:
    print('You lose')
