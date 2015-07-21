# Given a set of candidate numbers (C) and a target number (T), find all 
# unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# Time Complexity: O(n^n)
# Space Complexity: O(n^n)

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        cnt, items, DP = {}, [], [[] for _ in xrange(target + 1)]
        for key in sorted(candidates):
            cur = 1
            while cur * key <= target:
                items.append((cur * key, key, cur))
                cur *= 2
        for key, ori, ct in items:
            for i in xrange(target, key - 1, -1):
                DP[i].extend((p + [(key, ori, ct)] for p in DP[i - key]))
            DP[key].append([(key, ori, ct)])
        for i in xrange(len(DP[target])):
            DP[target][i] =  \
                  sum(([key] * count for (_, key, count) in DP[target][i]), [])
        return DP[target]

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum([2, 3, 6, 7], 7)
