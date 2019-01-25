
import random

# I am commenting


def showBoard(board):
    # print out a tic-tac-toe board
    print('_'*12)
    print('|', board[0], '|', board[1], '|', board[2])
    print('|', board[3], '|', board[4], '|', board[5])
    print('|', board[6], '|', board[7], '|', board[8])
    # return an empty string to avoid outputting the string 'None'
    return ''


def assign_symbols():
    # assign 'X' and 'O' randomly using the random library class
    possible_symbols = ['X', 'O']
    user_symbol = possible_symbols[random.randint(0, 1)]
    # assign the user's symbol by randomly selecting one of the elements
    # of the possible symbols list

    possible_symbols.remove(user_symbol)
    # remove the previously assigned symbol from the list
    # of possible symbols

    computer_symbol = possible_symbols[0]
    return [user_symbol, computer_symbol]


symbols = assign_symbols()
user_symbol = symbols[0]
computer_symbol = symbols[1]


def make_a_move(board):

    # allow the user to choose a space on the tic-tac-toe board

    userinput = input('Pick a space: ')
    # store the position chosen by the user
    try:
        position = int(userinput)

    except:
        return 'Invalid input. Please try again'

    if not position in board:
        return "The space chosen does not exist on the board. Please try again."
    # check to see whether the specified position actually lies on the board

    board[position - 1] = user_symbol
    return showBoard(board)


def createDiagonals(board):
    # store the diagonals of the board in a list
    # where the first element is a list of the diagonal running left to right
    # and the second element is a list of the diagonal running right to left

    first_diagonal = [board[0], board[4], board[8]]
    second_diagonal = [board[2], board[4], board[6]]
    diagonals = [first_diagonal, second_diagonal]
    return diagonals


def createCols(board):
    # store the columns of the board in a list
    # where each of the three elements is one of the columns
    # from left to right

    first_col = [board[0], board[3], board[6]]
    second_col = [board[1], board[4], board[7]]
    third_col = [board[2], board[5], board[8]]
    cols = [first_col, second_col, third_col]
    return cols


def createBoardData(board):
    # store the rows, columns, and diagonals of the board in a dictionary
    # where each key is either 'rows', 'columns', or 'diagonals'
    # and each value is the respective list
    dataDictionary = {}
    dataDictionary['rows'] = board[0:3], board[3:6], board[6:9]

    cols = createCols(board)
    dataDictionary['columns'] = cols[0], cols[1], cols[2]

    diagonals = createDiagonals(board)
    dataDictionary['diagonals'] = diagonals[0], diagonals[1]

    return dataDictionary


def check_solved(board):
    # check to see whether the board has been solved
    boardData = createBoardData(board)
    rows = boardData['rows']

    for row in rows:
        # loop through each of the rows to see if any have
        # three consective 'X's or 'O's
        if row.count('X') == 3 or row.count('O') == 3:
            return True

    columns = boardData['columns']
    for column in columns:
        # loop through the columns just as we did for rows
        if column.count('X') == 3 or column.count('O') == 3:
            return True

    diagonals = boardData['diagonals']
    for diagonal in diagonals:
        if diagonal.count('X') == 3 or diagonal.count('O') == 3:
            return True
    return False


def checkTied(board):
    # check to see whether their is a tie and neither player can win
    boardData = createBoardData(board)
    rows = boardData['rows']

    for row in rows:
        # check to see if both an X and O occur in each of the rows
        # if not, return False
        if 'X' not in row or 'O' not in row:
            return False

    columns = boardData['columns']
    for column in columns:
        # loop through the columns just as we did for the rows
        if 'X' not in column or 'O' not in column:
            return False

    diagonals = boardData['diagonals']
    for diagonal in diagonals:
        if 'X' not in diagonal or 'O' not in diagonal:
            return False
    # if we have passed all of the tests so far
    # it must still be possible to win
    return True


def countWaysToWin(board, position):
    # given a position on the board
        # determine how many rows of three can be acheived
        # from that position on the board
    boardData = createBoardData(board)
    ways_to_win = 0
    # create a variable ways_to_win that stores the number of
    # possible rows of three from a position
    rows = boardData['rows']
    # store the rows in the current board
    columns = boardData['columns']
    # store the columns in the current board
    diagonals = boardData['diagonals']
    # store the diagonals of the current board

    for row in rows:
        if position in row:
            if user_symbol not in row:
                ways_to_win += 1
                # if there are no 'O' in the position's row
                # increase ways to win by one
        # repeat the same procedure for the columns and diagonals

    for column in columns:
        if position in column:
            if user_symbol not in column:
                ways_to_win += 1

    for diagonal in diagonals:
        if position in diagonal:
            if user_symbol not in diagonal:
                ways_to_win += 1

    return ways_to_win


def find_best_spot(board):
    # loop through the entire board
    # and return the spot with the most ways to win
    best_spot = 0
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


def computer_move(board):
        # tell the computer to pick the best_spot available
        # on the tic-tac-toe board

    best_spot = find_best_spot(board)
    board[best_spot - 1] = computer_symbol
    return showBoard(board)


def game():
    # a list of instructions of how to run the game
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(showBoard(board))

    while True:
        if check_solved(board):
            user_input = input(
                'Game over. Type Yes if you would like to keep playing. Type No if you are done')
            if str(user_input) == 'Yes':
                board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                break

        if checkTied(board):
            user_input = input(
                "Cat's game. No one wins. Type Yes if you would like to keep playing. Type No if you are done")
            if str(user_input) == 'Yes':
                board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                break

        print(make_a_move(board))
        print(computer_move(board))

    return "Thanks for playing"


def game():
    # a list of instructions of how to run the game
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(showBoard(board))

    while True:
        if check_solved(board):
            user_input = input(
                'Game over. Type Yes if you would like to keep playing. Type No if you are done')
            if 'Yes' in str(user_input):
                board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                break

        if checkTied(board):
            user_input = input(
                "Cat's game. No one wins. Type Yes if you would like to keep playing. Type No if you are done")
            if 'Yes' in str(user_input):
                board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            else:
                break

        print(make_a_move(board))
        print(computer_move(board))

    return "Thanks for playing"


if __name__ == '__main__j':
    print("We got this far")
    print(game())
