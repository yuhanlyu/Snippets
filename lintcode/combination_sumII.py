class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
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
