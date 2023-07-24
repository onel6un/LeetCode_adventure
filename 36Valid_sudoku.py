from pprint import pprint
from typing import List


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self._check_rows(board)
            and self._check_sub_boxes(board)
            and self._check_cols(board)
        )

    def _check_rows(self, board) -> bool:
        for row in board:
            check_set = set()
            for cell in row:
                if cell == ".":
                    continue
                if cell not in check_set:
                    check_set.add(cell)
                else:
                    return False
        return True

    def _check_cols(self, board) -> bool:
        for col in range(9):
            check_set = set()
            for row in range(9):
                item = board[row][col]
                if item == ".":
                    continue
                if item not in check_set:
                    check_set.add(item)
                else:
                    return False
        return True

    def _check_sub_boxes(self, board):
        for r in range(0, 7, 3):
            for c in range(0, 7, 3):
                check_set = set()
                for row in range(r, 3 + r):
                    for col in range(c, 3 + c):
                        item = board[row][col]
                        if item == ".":
                            continue
                        if item not in check_set:
                            check_set.add(item)
                        else:
                            return False
        return True

sudoku = [[".",".","4",".",".",".","6","3","."],
          [".",".",".",".",".",".",".",".","."],
          ["5",".",".",".",".",".",".","9","."],
          [".",".",".","5","6",".",".",".","."],
          ["4",".","3",".",".",".",".",".","1"],
          [".",".",".","7",".",".",".",".","."],
          [".",".",".","5",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]]

s = Solution()
pprint(s.isValidSudoku(sudoku))
