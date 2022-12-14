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
    X = player.board
    currentPlayer = X
    if currentPlayer == X:
        currentPlayer = O
    return currentPlayer
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    currentPlayer = player(board)
    for i in range(3):
        if self.board[i][0] == self.board[i][1] == self.board[i][2] == currentPlayer:
            return True
        if self.board[0][i] == self.board[1][i] == self.board[2][i] == currentPlayer:
            return True

    if self.board[0][0] == self.board[1][1] == self.board[2][2] == currentPlayer:
        return True
    if self.board[0][2] == self.board[1][1] == self.board[2][0] == currentPlayer:
        return True

    return False
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner == True:
        return True
    else:
        return False
    raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        player = winner(board)
        if player == O:
            return -1
        elif player == X:
            return 1
        else:
            return 0
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
