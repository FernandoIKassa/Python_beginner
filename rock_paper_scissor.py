from random import choice

list_choices = ['r', 'p', 's']

def run_game():
    player = ''
    computer = ''
    player = input('Choose rock(R), paper(P) or scissors(S)\n').lower()
    computer = choice(list_choices)
    if player == computer:
        print(f'The computer chose {computer}')
        print('Tie!')
        return True
    if to_win(player, computer):
        print(f'The computer chose {computer}')
        print('You won!')
        return True
    return print(f'The computer chose {computer}' + '\nÝou lost!')

def to_win(player, computer):
    #rock > scissor
    #paper > rock
    #scissor > paper
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

run_game()