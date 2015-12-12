# Say you have an array for which the ith element is the price of a given 
# stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many 
# transactions as you like (ie, buy one and sell one share of the stock 
# multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must 
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 
# day)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        free, have, cool = 0, float("-inf"), float("-inf")
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([1, 2, 3, 0, 2])
