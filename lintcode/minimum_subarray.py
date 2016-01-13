class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        result, cur = nums[0], 0
        for num in nums:
            cur, result = cur + num, min(result, cur + num)
            if cur > 0: cur = 0
        return result
                
if __name__ == "__main__":
    solution = Solution()
    print solution.minSubArray([1, -1, -2, 1])
