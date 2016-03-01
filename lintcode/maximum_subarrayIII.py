import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        if sum([1 for num in nums if num > 0]) <= k:
            return sum(heapq.nlargest(k, nums))
        prices = [0]
        for num in nums:
            prices.append(prices[-1] + num)
        result, low, high, stack, profits = 0, 0, 0, [], []
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
