class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def helper(row, col, visited, word, level):
            if not (0 <= row < len(board))     \
            or not (0 <= col < len(board[row])) \
            or visited[row][col] or board[row][col] != word[level]:  
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
