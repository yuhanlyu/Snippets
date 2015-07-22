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
        DP = [[] for _ in xrange(target + 1)]
        for candidate in sorted(x for x in candidates if x <= target):
            DP[candidate].append([candidate])
            for key in xrange(candidate, target + 1):
                DP[key].extend(p + [candidate] for p in DP[key - candidate])
        return DP[target]

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum([2], 1)
    print solution.combinationSum([2, 3, 6, 7], 7)
