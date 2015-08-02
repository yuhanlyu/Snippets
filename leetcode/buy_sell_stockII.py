# Say you have an array for which the ith element is the price of a given 
# stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many 
# transactions as you like (ie, buy one and sell one share of the stock 
# multiple times). However, you may not engage in multiple transactions at the 
# same time (ie, you must sell the stock before you buy again).
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        result = 0
        for i in xrange(1, len(prices)):
            result += max(0, prices[i] - prices[i - 1])
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([1,3,2])
