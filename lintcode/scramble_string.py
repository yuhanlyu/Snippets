class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        L = [[set([j for j in xrange(len(s2)) if s1[i] == s2[j]])
                     for i in xrange(len(s1))]]
        for k in xrange(1, len(s1)):
            L.append([set() for _ in xrange(len(s1) - k)])
            for i in xrange(len(s1) - k):
                for m in xrange(k):
                    for j in L[m][i]:
                        if j + m + 1 in L[k - m - 1][i + m + 1]:
                            L[k][i].add(j)
                        if j - k + m in L[k - m - 1][i + m + 1]:
                            L[k][i].add(j - k + m)
        return len(L[-1][-1]) > 0
