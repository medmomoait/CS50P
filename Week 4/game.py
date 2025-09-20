from sys import exit
from random import randint

def guessing_game():

    while True:
        try:
            level = int(input('Level: '))
        except ValueError:
            continue
        else:
            if level == 0 or level < 0:
                continue
            else:
                break
    game = randint(1, level)

    while True:
        try:
            guess = int(input('Guess: '))

        except ValueError:
            pass

        else:
            if guess > game:
                print('Too large!')
            elif guess < game:
                print('Too small!')
            else:
                print('Just right!')
                break

guessing_game()