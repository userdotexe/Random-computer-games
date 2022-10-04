import random

def play():
    user = input("Make a move! 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user,computer):
        return 'You won! wew :>'

    return 'You lost :('
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
