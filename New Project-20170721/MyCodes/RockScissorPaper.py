# RockScissorPaper Game

First_Player = input('Enter your choice from paper, scissor, and rock: ', )
Second_Player = input('Enter your choice from paper, scissor, and rock: ', )

if First_Player.upper() == Second_Player.upper():
    print('Game is a Draw')
elif First_Player.upper() == 'ROCK' and Second_Player.upper() == 'SCISSOR':
    Print('First_Player is the winner!')
elif First_Player.upper() == 'SCISSOR' and Second_Player.upper() == 'PAPER':
    print('First_Player is the winner!')
elif First_Player.upper() == 'PAPER' and Second_Player.upper() == 'ROCK':
    print('First_Player is the winner!')
elif Second_Player.upper() == 'ROCK' and First_Player.upper() == 'SCISSOR':
    print('Second_Player is the winner!')
elif Second_Player.upper() == 'SCISSOR' and First_Player.upper() == 'PAPER':
    print('Second_Player is the winner!')
elif Second_Player.upper() == 'PAPER' and First_Player.upper() == 'ROCK':
    print('Second_Player is the winner!')
else:
    print ('No Idea')