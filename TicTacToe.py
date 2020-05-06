#! python3
# TicTacToe.py - A basic Tic-Tac-Toe game.

import random

# Create an empty board
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# Function to create the board layout (dividers)
def display_board(board):
    print(board[1]+' ┃'+board[2]+' ┃'+board[3])
    print(''+ '━━''╋'+'━━'+'╋'+ '━━')
    print(board[4]+' ┃'+board[5]+' ┃'+board[6])
    print(''+ '━━''╋'+'━━'+'╋'+ '━━')
    print(board[7]+' ┃'+board[8]+' ┃'+board[9])

# Function to choose player markers
def player_input():
    global marker
    global player2
    global player1
    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1 = marker

    if marker == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(f'Player 2, you are {player2}. Let us begin!')

# Function to decide who goes first by choosing a random number
def who_goes_first():
    x = random.randint(0,1)

    if x == 0:
        return('Player 1, you go first!')
    else:
        return('Player 2, you go first!')

# Function to define player 1's marker
def place_marker(board, player1, position):
    board[position] = player1
    return board


# Function to define player 2's marker
def place_marker_p2(board, player2, position):
    board[position] = player2
    return position

# Function to define an open space on the board
def open_space(board,position):
    if board[position] != ' ':
        return False

# Function to define player's choice of position
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not open_space(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position

# Function to check for wins
def win_check(board,character):

    return((board[1] == character and board[2] == character and board[3] == character) ## across the top
    or (board[4] == character and board[5] == character and board[6] == character) ## across the middle
    or (board[7] == character and board[8] == character and board[9] == character) ## across the bottom
    or (board[1] == character and board[5] == character and board[9] == character) ## diagonally from top left to bottom
    or (board[3] == character and board[5] == character and board[7] == character) ## diagonally from top right to bottom
    or (board[1] == character and board[4] == character and board[7] == character) ## down left
    or (board[2] == character and board[5] == character and board[8] == character) ## down middle
    or (board[3] == character and board[6] == character and board[9] == character)) ## down right



# Function to check if the board is full
def full_board():

    for p in board:
        if ' ' not in board:
            return True
        else:
            return False

# Function to ask the players if they would like to play again
def replay():
    return input('Do you want to play again?').lower().startswith('y')


# Start the game
print('Welcome to Tic-Tac-Toe!')

while True:
    # Reset the board
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    # Choose player markers ('X' or 'O')
    player_input()
    # Randomly decide who goes first
    turn = who_goes_first()
    lets_play = input('Are you ready to play? Type Yes or No: ')
    if lets_play.lower()[0] == 'y':
        game = True
    else:
        game = False

    while game:
        if turn == 'Player 1, you go first!':
            # Display the current board
            display_board(board)
            # Ask the player where they would like to place their marker
            player_choice(board)
            # Place the marker based on the player's input
            place_marker(board, player1, position)
            # Display the updated board
            diplay_board(board)

            # Check if there is a win
            if win_check(board, player1):
                display_board(board)
                print("Congratulations, you've won the game!")
                game = False
            else:
                # Check if the board is full
                if full_board(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 2, you go first!'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker_p2(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print("Congratulations, you've won the game!")
                game = False
            else:
                if full_board(board):
                    display_board(board)
                    print("It's a draw!")
                    break
                else:
                    turn = 'Player 2, you go first!'

    if not replay():
        break
