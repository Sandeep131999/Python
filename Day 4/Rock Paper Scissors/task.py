import random
from random import randint

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
# Add to a Python list
choices = [rock, paper, scissors]
#Basic Game rules of the game
# 0 -> Rock     # Rock wins against scissors.
# 1 -> Paper    # Paper wins against rock.
# 2 -> scissors # Scissors win against paper.
chose_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
rand_num = random.randint(0,2)
print(choices[chose_option])
print("Computer chose")
print(choices[rand_num])
if chose_option == 0 or chose_option == 1 or chose_option == 2 :
    if (chose_option == 0 and rand_num == 2) or \
       (chose_option == 1 and rand_num == 0) or \
       (chose_option == 2 and rand_num == 1):
        print("You win")
    elif (chose_option == 0 and rand_num == 1) or \
         (chose_option == 1 and rand_num == 2) or \
         (chose_option == 2 and rand_num == 0):
        print("Computer wins")
    elif chose_option == rand_num:
        print("It's a tie!")

else:
    print("Please choose a correct option")



