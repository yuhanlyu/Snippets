class Solution:
    # @param n: An integer.
    # return : A list of integer storing 1 to the largest number with n digits.
    def numbersByRecursion(self, n):
        if n == 0: return []
        return list(xrange(1, 10)) + \
               [n * 10 + x for n in self.numbersByRecursion(n - 1) 
                           for x in xrange(10)]
