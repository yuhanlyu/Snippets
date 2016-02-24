class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        DP = [[] for _ in xrange(target + 1)]
        for candidate in sorted(x for x in candidates if x <= target):
            DP[candidate].append([candidate])
            for key in xrange(candidate, target + 1):
                DP[key].extend(p + [candidate] for p in DP[key - candidate])
        return DP[target]
