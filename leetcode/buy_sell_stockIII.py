# Say you have an array for which the ith element is the price of a given stock
# on day i.
# Design an algorithm to find the maximum profit. You may complete at most two 
# transactions.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        buy1, buy2, sell1, sell2 = -2 ** 32, -2 ** 32, 0, 0
        for price in prices:
            buy2, sell2 = max(buy2, sell1 - price), max(sell2, buy2 + price)
            buy1, sell1 = max(buy1,       - price), max(sell1, buy1 + price)
        return sell2

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([3,1,2,4])
