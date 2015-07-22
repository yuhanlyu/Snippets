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
        def plus_one(lists):
            return ([x + 1 for x in l] for l in lists if l[-1] < 9)
        DP = [[[] for _ in xrange(k + 1)] for _ in xrange(n + 1)]
        DP[1][1].append([1])
        for i in xrange(1, n + 1):
            for j in xrange(1, min(k + 1, i)):
                DP[i][j].extend(plus_one(DP[i - j][j]))
                DP[i][j].extend([1] + p for p in plus_one(DP[i - j][j - 1]))
        return DP[n][k]

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum3(3, 7)
    print solution.combinationSum3(3, 9)
