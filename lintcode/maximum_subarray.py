class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    def maxSubArray(self, nums):
        result, cur = nums[0], 0
        for num in nums:
            cur, result = cur + num, max(result, cur + num)
            if cur < 0: cur = 0
        return result
                
if __name__ == "__main__":
    solution = Solution()
    print solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
