import random

random_number = random.randint(1, 30)
user_number = int(input('Your number (from 1 to 30): '))

if user_number == random_number:
    print('You right!')

else:
    print('Your guess is wrong :(')
