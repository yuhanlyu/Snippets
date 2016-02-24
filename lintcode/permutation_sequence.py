class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        fac, result = 1, [i + 1 for i in xrange(n)]
        for i in xrange(2, n):
            fac *= i
        k -= 1
        for i in xrange(n - 1):
            (d, k) = divmod(k, fac)
            if d: result[i:i + d + 1] = [result[i + d]] + result[i:i + d]
            fac /= (n - 1 - i)
        return ''.join([str(x) for x in result])
