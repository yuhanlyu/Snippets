# Find the contiguous subarray within an array (containing at least one number)
# which has the largest sum.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        result, cur = nums[0], 0
        for num in nums:
            cur, result = cur + num, max(result, cur + num)
            if cur < 0: cur = 0
        return result
                

if __name__ == "__main__":
    solution = Solution()
    print solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
