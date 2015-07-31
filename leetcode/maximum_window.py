# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers 
# in the window. Each time the sliding window moves right by one position.
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        queue, result = deque(), []
        for i, num in enumerate(nums):
            if queue and queue[0] == i - k: queue.popleft()
            while queue and num >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k - 1: result.append(nums[queue[0]])
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
