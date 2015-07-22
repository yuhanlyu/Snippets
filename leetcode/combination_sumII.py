# Given a collection of candidate numbers (C) and a target number (T), 
# find all unique combinations in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# Time Complexity: O(n^n)
# Space Complexity: O(n^n)

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        DP, cnt = [[] for _ in xrange(target + 1)], {}
        for c in (item for item in candidates if item <= target):
            cnt[c] = cnt.get(c, 0) + 1
        for c in sorted(cnt.keys()):
            for t in xrange(1, cnt[c] + 1):
                if t * c > target: break
                DP[t * c].append([c] * t)
                for key in xrange(target, t * c - 1, -1):
                    DP[key].extend((p + [c] * t for p in DP[key - c * t]
                                    if p[-1] != c))
        return DP[target]

if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum2([10,1,2,7,6,1,5], 8)
