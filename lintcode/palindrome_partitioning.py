class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        def helper(s, DP, index, cur, result):
            if index == len(s):
                result.append(list(cur))
            else:
                for i in xrange(index, len(s)):
                    if DP[index][i]:
                        cur.append(s[index:i + 1])
                        helper(s, DP, i + 1, cur, result)
                        cur.pop()
            return result
        DP = [[False] * len(s) for _ in xrange(len(s))]
        for i in xrange(len(s)):
            DP[i][i] = True
        for k in xrange(1, len(s)):
            for i in xrange(len(s) - k):
                if (k == 1 or DP[i + 1][i + k - 1]) and s[i] == s[i + k]:
                    DP[i][i + k] = True
        return helper(s, DP, 0, [], [])
