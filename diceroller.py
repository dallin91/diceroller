# This project will simulate a dice roll
# Creator: Dallin Reeves
# April 8, 2019 1:57PM

import random
min = 1
max = 6

roll = input('Would you like to roll? ')

while roll.lower() == 'yes' or roll.lower() == 'y':
    print('Rolling your lucky number.......')
    print('You rolled ', random.randint(min, max), '!')

    roll = input('Would you like to roll again? ')

print("Thanks for playing!")