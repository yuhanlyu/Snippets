class Solution:
    #@param n, m: Two integer
    #@param i, j: Two bit positions
    #return: An integer
    def updateBits(self, n, m, i, j):
        mask = ((1 << 32) - 1) - ((1 << (j + 1)) - 1) + ((1 << i) - 1)
        ans = (n & mask) + (m << i)
        return ans - (1 << 32) if ans > 0 and ans & (1 << 31) else ans
