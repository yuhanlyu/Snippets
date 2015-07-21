# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 
# 'X'. A region is captured by flipping all 'O's into 'X's in that surrounded 
# region.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        if not board: return
        stack = [(i, j) for i in (0, len(board) - 1)
                        for j in xrange(len(board[i])) if board[i][j] == 'O']
        stack.extend(((i, j) for i in xrange(1, len(board) - 1)
                             for j in (0, len(board[i]) - 1)
                             if board[i][j] == 'O'))
        for i, j in stack:
            board[i][j] = 'N'
        while stack:
            row, col = stack.pop()
            for i, j in ((row + dr, col + dc) for (dr, dc) in 
                          ((0, 1), (0, -1), (1, 0), (-1, 0))
                          if 0 <= row + dr < len(board) and
                             0 <= col + dc < len(board[row + dr]) and
                             board[row + dr][col + dc] == 'O'):
                board[i][j] = 'N'
                stack.append((i, j))
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

if __name__ == "__main__":
    board = [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")]
    solution = Solution()
    solution.solve(board) 
    print board
