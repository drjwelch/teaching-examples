# Noughts and crosses game

import random

# board will contain a 2D array of integers
# 0 for empty, 1 for X and 2 for O

board = []

# symbol is the corresponding symbol to the number stored in board
# symbol[0] = empty (space), symbol[1] = 'X' and symbol[2] = 'O'

symbol = " XO"

# make some constants - they could be any numbers, it's just so we can write words that make sense
# in our code to make it readable

COMPUTER = 1
HUMAN = -1

# define functions and procedures

def get_yn_answer():
    ans = 'x'
    while ans not in 'yn':
        ans = input().lower()[0]
    return ans
        
def show_grid(f):
    print("+---+---+---+")
    for row in range(3):
        for column in range(3):
            print("+ "+f(row,column)+" ",end='')
        print("+\n",end='')
    print("+---+---+---+")

def syms(r,c):
    return symbol[board[r][c]]
    
def nums(r,c):
    return str(r*3+c+1)
    
def show_board():
    show_grid(syms)

def ask_who_first():
    print("Do you want to go first? [y/n] ")
    if get_yn_answer() == 'y':
        return HUMAN
    else:
        return COMPUTER

def is_it_empty(s):
    if s in '123456789':
        s = int(s)-1
        return board[s//3][s%3]==0
    else:
        return False

def make_move(who,whoisX,s):
    if s in '123456789':
        s = int(s)-1
        if who == whoisX:
            board[s//3][s%3] = 1 # X
        else:
            board[s//3][s%3] = 2 # O
    else:
        print("HELP!")
        
def humanmove(playerX):
    print("Where do you want to go?")
    show_grid(nums)
    square = ' '
    while square not in '123456789' or is_it_empty(square) == False:
        square = input()[0]
    make_move(HUMAN,playerX,square)

def computermove(playerX):
    print("Thinking ...")
    square = '99'
    while is_it_empty(square) == False:
        square = str(random.randint(1,9))
    make_move(COMPUTER,playerX,square)
        
def check_if_won(whoisX):
    if board[0][0]*board[1][1]*board[2][2] in (1,8) or \
        board[0][2]*board[1][1]*board[2][0] in (1,8) or \
        board[1][0]*board[1][1]*board[1][2] in (1,8) or \
        board[0][1]*board[1][1]*board[2][1] in (1,8):
            if board[1][1] == 1:
                return whoisX
            else:
                return -whoisX
    if board[0][0]*board[1][0]*board[2][0] in (1,8) or \
        board[0][0]*board[0][1]*board[0][2] in (1,8):
            if board[0][0] == 1:
                return whoisX
            else:
                return -whoisX
    if board[2][0]*board[2][1]*board[2][2] in (1,8) or \
        board[0][2]*board[1][2]*board[2][2] in (1,8):
            if board[2][2] == 1:
                return whoisX
            else:
                return -whoisX
    return False # no winner

def ask_to_play_again():
    print("Play again?")
    if get_yn_answer()=='y':
        return True
    else:
        return False
    
# Start the game

play_again = True

while play_again:

    board = [ [0,0,0] , [0,0,0] , [0,0,0] ]
    turns_taken = 0
    game_over = False
    player = ask_who_first()
    who_is_X = player # X always goes first

    while not game_over:
        show_board()
        if player == HUMAN:
            humanmove(who_is_X)
            player = COMPUTER
        else:
            computermove(who_is_X)
            player = HUMAN
        winner = check_if_won(who_is_X)
        if winner != False:
            show_board()
            if winner == HUMAN:
                print("You win!")
            else:
                print("You lose!")
            game_over = True
        turns_taken += 1
        if turns_taken == 9:
            game_over = True

    play_again = ask_to_play_again()

print("Thanks for playing OXO!")
        
