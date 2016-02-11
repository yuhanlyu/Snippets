class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        row, column, block = [0] * 9, [0] * 9, [0] * 9
        for i, board_row in enumerate(board):
            for j, e in enumerate(board_row):
                if e != '.':
                    mask = 1 << int(e)
                    block_i = (i / 3) * 3 + j / 3
                    if mask & (row[i] | column[j] | block[block_i]):
                        return False
                    row[i] |= mask
                    column[j] |= mask
                    block[block_i] |= mask
        return True
