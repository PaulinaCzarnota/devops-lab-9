def is_valid(board, row, col, num):
    """Check if placing num at (row, col) is valid according to Sudoku rules."""
    # Check if number is in the same row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check if number is in the 3x3 square
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    """Recursive backtracking solver that modifies the board in place."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Empty cell
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Try this number

                        if solve(board):      # Recur with this number
                            return True
                        board[row][col] = 0   # Backtrack

                return False  # No valid number found
    return True  # Board is fully solved

def is_board_valid(board):
    """Validate the initial board to ensure it's logically solvable."""
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
    Main function to validate the board and then solve it.
    Returns the solved board or None if unsolvable or invalid.
    """
    if not is_board_valid(board):
        return None
    if solve(board):
        return board
    return None