from collections import deque

class Solution:
    """
    @param nums: A list of integers.
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        queue, result = deque(), []
        for i, num in enumerate(nums):
            if queue and queue[0] == i - k: queue.popleft()
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k - 1: result.append(nums[queue[0]])
        return result
