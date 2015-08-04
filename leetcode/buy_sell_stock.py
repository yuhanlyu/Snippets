# Say you have an array for which the ith element is the price of a given 
# stock on day i.
# If you were only permitted to complete at most one transaction (ie, buy one 
# and sell one share of the stock), design an algorithm to find the maximum 
# profit.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if not prices: return 0
        result, m = 0, prices[0]
        for price in prices:
            result = max(result, price - m)
            m = min(m, price)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([1,3,2])
