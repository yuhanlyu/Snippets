# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination should 
# be a unique set of numbers.
# Time Complexity: O(9^9)
# Space Complexity: O(9^9)

class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        def feasible(n, k, l, h):
            return k * l + k * (k - 1) / 2 <= n <= k * h - k * (k - 1) / 2
        def min(n, k, l, h):
            result, nn = [0] * k, n
            for kk in xrange(k, 0, -1):
                for x in xrange(h, l - 1, -1):
                    if feasible(nn - x, kk - 1, l, x - 1):
                        nn -= x
                        result[kk - 1], h = x, x - 1
                        break
            return result
        if not feasible(n, k, 1, 9): return []
        solution = min(n, k, 1, 9)
        result = [list(solution)]
        while True:
            kk, sum = k - 2, solution[k - 1]
            while kk >= 0 and \
                not feasible(sum + solution[kk], k - kk, solution[kk] + 1, 9):
                sum += solution[kk]
                kk -= 1
            if kk < 0: break
            solution[kk] += 1
            solution[kk + 1:] = min(sum - 1, k - kk - 1, solution[kk] + 1, 9)
            result.append(list(solution))
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum3(3, 7)
    print solution.combinationSum3(3, 9)
    print solution.combinationSum3(3, 2)
