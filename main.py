SudokuBoard = []

# Taking input from the user
while True:
    row = list(input("Row : "))
    ints = []
    for n in row:
        ints.append(int(n))
    SudokuBoard.append(ints)

    if len(SudokuBoard) == 9:
        break
    print('Row ' + str(len(SudokuBoard)) + " Is Entered In The Sudoku Board")


def solve_sudoku(Board):
    find = find_blank_space(Board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if isValid(Board, i, (row, col)):
            Board[row][col] = i

            if solve_sudoku(Board):
                return True
            Board[row][col] = 0

    return False


def isValid(Board, num, position):
    # Checking if row is valid
    for i in range(len(Board[0])):
        if Board[position[0]][i] == num and position[1] != i:
            return False

    # Checking if Column is valid
    for i in range(len(Board)):
        if Board[i][position[1]] == num and position[0] != i:
            return False

    # Checking in the Box of 3 * 3 box if number is valid
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if Board[i][j] == num and (i, j) != position:
                return False

    return True


# Printing the Soduku board
def print_sudoku(Board):
    for i in range(len(Board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(Board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(Board[i][j])
            else:
                print(str(Board[i][j]) + " ", end="")


# Finding Blank Spaces in the Sudoku Board
def find_blank_space(Board):
    for i in range(len(Board)):
        for j in range(len(Board[0])):
            if Board[i][j] == 0:
                return i, j

    return None


print("\nSudoku Puzzle Before: \n")
print_sudoku(SudokuBoard)
solve_sudoku(SudokuBoard)
print("\nSudoku Puzzle After using Backtracking algorithm: \n")
print_sudoku(SudokuBoard)
