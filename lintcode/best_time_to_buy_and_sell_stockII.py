class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        result = 0
        for i in xrange(1, len(prices)):
            result += max(0, prices[i] - prices[i - 1])
        return result
