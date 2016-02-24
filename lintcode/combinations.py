class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        result, x = [], (1 << k) - 1
        while x < (1 << n):
            result.append([i + 1 for i in xrange(n) if ((x >> i) & 1)])
            u = x & -x
            v = u + x
            x = v | (((v^x) / u) >> 2)
        return result
