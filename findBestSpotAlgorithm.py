import random

board = [1, 2, 3, 4, 5, 6, 7, 8, 9
         ]


def checkOpponentAboutToWin(board, opponent_symbol, player_symbol):
        # if your opponent is about to win, return the last spot
        # otherwise, return False
    boardData = createBoardData(board)
    rows = boardData['rows']
    columns = boardData['columns']
    diagonals = boardData['diagonals']

    for row in rows:
        if row.count(opponent_symbol) == 2 and row.count(player_symbol) == 0:
            for position in row:
                if type(position) == int:
                    return position

    for column in columns:
        if column.count(opponent_symbol) == 2 and column.count(player_symbol) == 0:
            for position in column:
                if type(position) == int:
                    return position

    for diagonal in diagonals:
        if diagonal.count(opponent_symbol) == 2 and diagonal.count(player_symbol) == 0:
            for position in diagonal:
                if type(position) == int:
                    return position

    return False

# Instead of creating a separate procedure for checking if you are about to win,
# use the checkOpponentAboutToWin procedure but passing in your own symbol as the second parament
#checkOpponentAboutToWin(board, player_symbol, opponent_symbol)


def find_best_spot(board):
        # def find_best_spot(board):

    # loop through the entire board

    # and return the spot with the most ways to win

    best_spot = None

    most_ways_to_win = 0

    spots_left = [i for i in board if type(i) == int]

    # make sure to only loop through positions that are still available

    # that is, only positions that are still labeled with an integer

    for position in spots_left:

        ways_to_win = countWaysToWin(board, position)

        if ways_to_win > most_ways_to_win:

            most_ways_to_win = ways_to_win

            best_spot = position

    return best_spot
