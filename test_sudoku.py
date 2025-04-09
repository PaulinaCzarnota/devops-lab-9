import unittest
from sudoku import solve_sudoku

class TestSudokuSolver(unittest.TestCase):

    def test_easy_puzzle(self):
        """Simple solvable puzzle (e.g., from sudoku.com)."""
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
        """A puzzle that's already solved."""
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
        self.assertEqual(solve_sudoku(solved_board), solved_board)

    def test_invalid_board(self):
        """Board that breaks Sudoku rules (duplicate values)."""
        invalid = [[5] * 9 for _ in range(9)]
        self.assertIsNone(solve_sudoku(invalid))

    def test_empty_board(self):
        """Completely empty puzzle."""
        board = [[0] * 9 for _ in range(9)]
        self.assertIsNotNone(solve_sudoku(board))

    def test_real_puzzle(self):
        """Puzzle from anysudokusolver.com."""
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
        self.assertIsNotNone(solve_sudoku(puzzle))

    def test_wikipedia_puzzle(self):
        """Test Wikipedia example puzzle."""
        wiki = [
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
        self.assertIsNotNone(solve_sudoku(wiki))


if __name__ == '__main__':
    unittest.main()