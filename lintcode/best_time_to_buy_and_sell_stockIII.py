class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        buy1, buy2, sell1, sell2 = -2 ** 32, -2 ** 32, 0, 0
        for price in prices:
            buy2, sell2 = max(buy2, sell1 - price), max(sell2, buy2 + price)
            buy1, sell1 = max(buy1,       - price), max(sell1, buy1 + price)
        return sell2
