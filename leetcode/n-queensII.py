# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total number of 
# distinct solutions.

class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        def helper(y, count):
            if y == n:
                count[0] += 1
            else:
                for x in xrange(n):
                    if not mx[x] and not d1[x + y]  and not d2[n - 1 + x - y]:
                        mx[x] = d1[x + y] = d2[n - 1 + x - y] = True
                        helper(y + 1, count)
                        mx[x] = d1[x + y] = d2[n - 1 + x - y] = False
            return count
        mx, d1, d2, count = [False] * n, [False] * (2 * n), [False] * (2 * n), 0
        return helper(0, [0])[0]

if __name__ == "__main__":
    solution = Solution()
    print solution.totalNQueens(12)
