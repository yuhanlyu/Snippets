# Say you have an array for which the ith element is the price of a given stock 
# on day i.
# Design an algorithm to find the maximum profit. You may complete at most k 
# transactions.
# Time Complexity: O(n lg n), (O(n) is doable by using linear time selection)
# Space Complexity: O(n)

import heapq

class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, k, prices):
        low, high, stack, profits = 0, 0, [], []
        while high + 1 < len(prices):
            low = high
            while low < len(prices) - 1 and prices[low] >= prices[low + 1]: 
                low += 1
            high = low
            while high < len(prices) - 1 and prices[high] < prices[high + 1]: 
                high += 1
            while stack and prices[low] < prices[stack[-1][0]]:
                profits.append(prices[stack[-1][1]] - prices[stack[-1][0]])
                stack.pop()
            while stack and prices[high] >= prices[stack[-1][1]]:
                profits.append(prices[stack[-1][1]] - prices[low])
                (low, _) = stack.pop()
            stack.append((low, high))
        while stack:
            profits.append(prices[stack[-1][1]] - prices[stack[-1][0]])
            stack.pop();
        return sum(heapq.nlargest(k, profits) if k < len(profits) else profits)

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit(2, [1,3,2, 4])
