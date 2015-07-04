# Determine if a Sudoku is valid
# Time Complexity: O(n^2)
# Space Complexity: O(n^2), in this problem n is a constant

class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        row = [[False] * 9 for _ in xrange(9)]
        column = [[False] * 9 for _ in xrange(9)]
        block = [[[False] * 9 for _ in xrange(3)] for _ in xrange(3)]
        for i, board_row in enumerate(board):
            for j, e in enumerate(board_row):
                if e != '.':
                    e = int(e) - 1
                    block_i, block_j = i / 3, j / 3
                    if row[i][e] == True or column[j][e] == True \
                    or block[block_i][block_j][e] == True:
                        return False
                    row[i][e] = column[j][e] = block[block_i][block_j][e] = True
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
