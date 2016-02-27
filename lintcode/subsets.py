class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        S.sort()
        return [[S[i] for i in xrange(len(S)) if (x >> i) & 1]
                         for x in xrange(0, 2 ** len(S))]
