class Solution:
    """
    Calculate the total number of distinct N-Queen solutions.
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
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
                    stack.extend([(y, x, True), (y + 1, 0, False)])
            else:
                mx[x] = d1[x + y] = d2[n - 1 + x - y] = False
        return result
