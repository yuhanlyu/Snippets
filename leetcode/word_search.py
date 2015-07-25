# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        def helper(row, col, visited, word, level):
            if row < 0 or row >= len(board) or col < 0 \
            or col >= len(board[row]) or visited[row][col] \
            or level >= len(word) or board[row][col] != word[level]: 
                return False
            if level == len(word) - 1: return True
            visited[row][col] = True
            for drow, dcol in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if helper(row + drow, col + dcol, visited, word, level + 1):
                    return True
            visited[row][col] = False
            return False
        visited = [[False] * len(board[0]) for _ in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if helper(i, j, visited, word, 0): return True
        return False

if __name__ == "__main__":
    solution = Solution()
    board = ["ABCE", "SFCS", "ADEE"]
    print solution.exist(board, "ABCCED")
    print solution.exist(board, "SEE")
    print solution.exist(board, "ABCB")
