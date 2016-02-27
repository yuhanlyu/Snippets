class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3): return False
        L = [0]
        for i in xrange(len(s3)):
            LL = []
            for j in L:
                if i - j < len(s2) and s2[i - j] == s3[i]:
                    if not LL or LL[-1] != j: LL.append(j)
                if j < len(s1) and s1[j] == s3[i]:
                    LL.append(j + 1)
            L = LL
        return len(s1) in L
