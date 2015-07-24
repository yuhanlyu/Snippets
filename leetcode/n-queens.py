# Given an integer n, return all distinct solutions to the n-queens puzzle.
# Each solution contains a distinct board configuration of the n-queens' 
# placement, where 'Q' and '.' both indicate a queen and an empty space 
# respectively.

class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        def helper(y, solution, result):
            if y == n:
                board = [["."] * n for _ in xrange(n)]
                for i in xrange(n):
                    board[i][solution[i]] = "Q"
                    board[i] = ''.join(board[i])
                result.append(board)
            else:
                for x in xrange(n):
                    if not mx[x] and not d1[x + y]  and not d2[n - 1 + x - y]:
                        mx[x] = d1[x + y] = d2[n - 1 + x - y] = True
                        solution[y] = x
                        helper(y + 1, solution, result)
                        mx[x] = d1[x + y] = d2[n - 1 + x - y] = False
            return result
        mx, d1, d2 = [False] * n, [False] * (2 * n), [False] * (2 * n)
        return helper(0, [-1] * n, [])

if __name__ == "__main__":
    solution = Solution()
    print solution.solveNQueens(4)
