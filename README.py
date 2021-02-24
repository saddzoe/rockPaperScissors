# rockPaperScissors
# A game of Rock Paper Scissors

import random

def play():
  user = input("Pick one of these. 'r' is for rock, 'p' is for paper, 's' is for scissors")
  computer = random.choice(['r', 'p', 's'])
  
  if user == computer:
    return 'Tie'

  if win(user, computer):
    return 'Congratulations! You win!"
  
  return 'Sorry, try again next time.'
  

def win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
    or (player == 'p' and opponent == 'r':
    return True
