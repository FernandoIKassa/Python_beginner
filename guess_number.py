from calendar import c
from random import randint

def user_guess(limit_number):
    secret_number = randint(1, limit_number)
    guess = 0
    while guess != secret_number:
        guess = int(input(f'Guess a number between 1 and {limit_number}:\n'))
        if guess < secret_number:
            print('Too low. Try again!')
        if guess > secret_number:
            print('Too high. Try again')
    print(f'You did it! The secret number is {secret_number}!')

def computer_guess(limit_number):
    low_number = 1
    high_number = limit_number
    feedback = 'x'
    
    while (feedback != 'c'):
        guess = int(randint(low_number, high_number))
        feedback = input(f'Is {guess} too low (L), too high (H) or correct (C)?').lower()
        if feedback == 'l':
            low_number = guess + 1
        elif feedback == 'h':
            high_number = guess - 1
        
    print(f'Congrats! The computer guessed the right number: {guess}')

#user_guess(100)
computer_guess(100)