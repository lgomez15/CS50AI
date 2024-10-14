"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    # Count the number of X's and O's on the board
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # If the number of X's is less than or equal to the number of O's, it's X's turn
    if x_count <= o_count:
        return X
    
    # Otherwise, it's O's turn
    return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Initialize an empty set to store the possible actions
    possible_actions = set()

    # Iterate through the board and add the empty cells to the set
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))


    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Get the current player
    current_player = player(board)

    # Create a deep copy of the board: a deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
    new_board = [row.copy() for row in board]

    # Update the board with the new action
    i, j = action
    new_board[i][j] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]
        
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
      # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return True
        
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != EMPTY:
            return True
        
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return True
    
    # Check if the board is full
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Get the winner of the game
    winner_player = winner(board)

    # If X has won, return 1
    if winner_player == X:
        return 1
    
    # If O has won, return -1
    if winner_player == O:
        return -1
    
    # Otherwise, return 0
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # If the game is over, return None
    if terminal(board):
        return None

    # Get the current player
    current_player = player(board)

    # If the current player is X, maximize the score
    if current_player == X:
        _, action = max_value(board)
        print(action)
        return action
    
    # If the current player is O, minimize the score
    if current_player == O:
        _, action = min_value(board)
        
        print(action)
        return action
    
    raise NotImplementedError

def max_value(board):
    """
    Returns the maximum utility value and action for X.
    """
    # If the game is over, return the utility value and None
    if terminal(board):
        return utility(board), None

    # Initialize the value to negative infinity
    value = -math.inf
    best_action = None

    # Iterate through the possible actions
    for action in actions(board):
        # Get the result of the action
        new_board = result(board, action)
        # Get the minimum value for the opponent
        min_val, _ = min_value(new_board)
        # Update the value and action if the minimum value is greater
        if min_val > value:
            value = min_val
            best_action = action


    return value, best_action

def min_value(board):
    """
    Returns the minimum utility value and action for O.
    """
    # If the game is over, return the utility value and None
    if terminal(board):
        return utility(board), None

    # Initialize the value to positive infinity
    value = math.inf
    best_action = None

    # Iterate through the possible actions
    for action in actions(board):
        # Get the result of the action
        new_board = result(board, action)
        # Get the maximum value for the opponent
        max_val, _ = max_value(new_board)
        # Update the value and action if the maximum value is smaller
        if max_val < value:
            value = max_val
            best_action = action

    return value, best_action
    
