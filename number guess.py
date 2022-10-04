import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:  '))
        if guess < random_number:
            print('Sorry guess again ^o^ Too low')
        elif guess > random_number:
            print('Sorry too high @_@')

    print(f'Woo! you guessed the number!! :D {random_number}')

guess(100000000000000)
