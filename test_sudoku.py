import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_easy_puzzle(self):
        """Test solving a simple Sudoku puzzle with only a few blanks."""
        board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        result = solve_sudoku(board)
        self.assertIsNotNone(result)

    def test_already_solved(self):
        """Check a valid, already-solved puzzle remains unchanged."""
        solved_board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        result = solve_sudoku(solved_board)
        self.assertEqual(result, solved_board)

    def test_invalid_board(self):
        """Detects an invalid puzzle with duplicates."""
        invalid_board = [[5] * 9 for _ in range(9)]
        result = solve_sudoku(invalid_board)
        self.assertIsNone(result)

    def test_empty_board(self):
        """Solves a fully empty board (takes longer)."""
        empty_board = [[0] * 9 for _ in range(9)]
        result = solve_sudoku(empty_board)
        self.assertIsNotNone(result)

    def test_one_solution(self):
        """Puzzle with one unique solution from anysudokusolver.com"""
        puzzle = [
            [0, 0, 0, 0, 0, 7, 0, 9, 0],
            [1, 0, 0, 4, 0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 5, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        result = solve_sudoku(puzzle)
        self.assertIsNotNone(result)