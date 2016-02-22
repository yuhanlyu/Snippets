class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        F = [i for i in xrange(len(word2) + 1)]
        for i in xrange(1, len(word1) + 1):
            left_top, F[0] = F[0], i
            for j in xrange(1, len(word2) + 1):
                left_top, F[j] = F[j], left_top if word1[i - 1] == word2[j - 1]\
                                       else 1 + min(F[j], F[j - 1], left_top)
        return F[-1]
