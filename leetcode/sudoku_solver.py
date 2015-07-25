# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.

class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solveSudoku(self, board):
        def helper(board, level, rt, ct, bt):
            if level == len(p): return True
            (i, j) = p[level]
            for x in "123456789":
                if x not in rt[i] and x not in ct[j] and x not in bt[i/3][j/3]:
                    map(set.add, (rt[i], ct[j], bt[i/3][j/3]), (x, x, x))
                    board[i][j] = x
                    if helper(board, level + 1, rt, ct, bt): return True
                    map(set.remove, (rt[i], ct[j], bt[i/3][j/3]), (x, x, x))
        p = [(i, j) for i in xrange(9) for j in xrange(9) if board[i][j] == '.']
        rt = [set() for _ in xrange(9)]
        ct = [set() for _ in xrange(9)]
        bt = [[set() for _ in xrange(3)] for _ in xrange(3)]
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.': 
                    map(set.add, (rt[i], ct[j], bt[i/3][j/3]), (x, x, x))
        helper(board, 0, rt, ct, bt)

if __name__ == "__main__":
    solution = Solution()
    board = [list("53..7...."),
             list("6..195..."),
             list(".98....6."),
             list("8...6...3"),
             list("4..8.3..1"),
             list("7...2...6"),
             list(".6....28."),
             list("...419..5"),
             list("....8..79")]
    solution.solveSudoku(board)
    print board
