#!/usr/bin/python3
# TicTacToe.py - A basic Tic-Tac-Toe game.

# Function to decide who goes first by choosing a random number
def who_goes_first():
    x = random.randint(0,1)

    if x == 0:
        return('Player 1, you go first!')
    else:
        return('Player 2, you go first!')



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
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # Choose player markers ('X' or 'O')
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')

    player1_sign = marker

    if marker == 'X':
        player2_sign = 'O'
    else:
        player2_sign = 'X'
    print(f'Player 2, you are {player2_sign}. Let us begin!')

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
            while True:
                position = int(input('Choose your next position: (1-9) '))
                if position not in range(1,10):
                    print('Pick a valid number (1-9)')
                    continue
                elif board[position] != ' ':
                    print('Please pick an empty space.')
                    continue
                else:
                    # Place the marker based on the player's input
                    board[position] = player1_sign
                    # Display the updated board
                    diplay_board(board)
                    break

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
            # Display the current board
            display_board(board)
            # Ask the player where they would like to place their marker
            while True:
                position = int(input('Choose your next position: (1-9) '))
                if position not in range(1,10):
                    print('Pick a valid number (1-9)')
                    continue
                elif board[position] != ' ':
                    print('Please pick an empty space.')
                    continue
                else:
                    # Place the marker based on the player's input
                    board[position] = player2_sign
                    # Display the updated board
                    diplay_board(board)
                    break

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
