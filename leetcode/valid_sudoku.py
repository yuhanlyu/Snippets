# Determine if a Sudoku is valid
# Time Complexity: O(n^2)
# Space Complexity: O(n), in this problem n is a constant

class Solution:
    # @param {character[][]} board
    # @return {boolean}
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

if __name__ == "__main__":
    solution = Solution()
    print solution.isValidSudoku(["53..7....",
                                  "6..195...",
                                  ".98....6.",
                                  "8...6...3",
                                  "4..8.3..1",
                                  "7...2...6",
                                  ".6....28.",
                                  "...419..5",
                                  "....8..79"])
