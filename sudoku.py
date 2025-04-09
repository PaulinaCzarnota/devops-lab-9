def is_valid(board, row, col, num):
    """
    Check if placing 'num' at board[row][col] is valid according to Sudoku rules.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve(board):
    """
    Recursively solve the Sudoku puzzle using backtracking.
    Returns True if solved, False otherwise.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0  # Backtrack
                return False  # No valid number found
    return True


def is_board_valid(board):
    """
    Validate that the initial board doesn't violate Sudoku rules.
    """
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != 0:
                board[row][col] = 0
                if not is_valid(board, row, col, num):
                    return False
                board[row][col] = num
    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle if valid. Return solved board or None.
    """
    if not is_board_valid(board):
        return None
    if solve(board):
        return board
    return None  # If unsolvable