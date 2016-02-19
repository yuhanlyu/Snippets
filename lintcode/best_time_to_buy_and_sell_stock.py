class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices: return 0
        result, m = 0, prices[0]
        for price in prices:
            result = max(result, price - m)
            m = min(m, price)
        return result
