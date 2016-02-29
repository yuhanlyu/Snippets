from heapq import heappush, heappushpop

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        h, i, result = (None, [], []), 1, []
        for num in nums:
            heappush(h[-i], -heappushpop(h[i], num * i))
            i *= -1
            result.append(-h[-1][0])
        return result
