# Given a board with m by n cells, each cell has an initial state live (1) or 
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia 
# article):
# Any live cell with fewer than two live neighbors dies, as if caused by 
# under-population.
# Any live cell with two or three live neighbors lives on to the next 
# generation.
# Any live cell with more than three live neighbors dies, as if by 
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if 
# by reproduction.
# Write a function to compute the next state (after one update) of the board 
# given its current state.
# Time Complexity: O(nm)
# Space Complexity: O(1)

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                count = 0
                for row in xrange(max(i - 1, 0), min(i + 2, len(board))):
                    for col in xrange(max(j - 1, 0), min(j + 2, len(board[i]))):
                        count += board[row][col] & 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                board[i][j] >>= 1

if __name__ == "__main__":
    solution = Solution()
    board = [[1, 1], [1, 0]]
    solution.gameOfLife(board)
    print board
