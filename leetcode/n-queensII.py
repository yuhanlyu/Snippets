# Follow up for N-Queens problem.
# Now, instead outputting board configurations, return the total number of 
# distinct solutions.

class Solution:
     # @param {integer} n
     # @return {integer}
     def totalNQueens(self, n):
        mx, d1, d2 = [False] * n, [False] * (2 * n), [False] * (2 * n)
        stack, solution, result = [(0, 0, False)], [0] * n, 0
        while stack:
            y, x, flag = stack.pop()
            if y == n and flag == False:
                result += 1
            elif not flag:
                if x + 1 < n: stack.append((y, x + 1, False))
                if not mx[x] and not d1[x + y]  and not d2[n - 1 + x - y]:
                    mx[x] = d1[x + y] = d2[n - 1 + x - y] = True
                    solution[y] = x
                    stack.append((y, x, True))
                    stack.append((y + 1, 0, False))
            else:
                mx[x] = d1[x + y] = d2[n - 1 + x - y] = False
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.totalNQueens(12)
