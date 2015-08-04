# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        result = cur_min = cur_max = nums[0]
        for i in xrange(1, len(nums)):
            (cur_min, _, cur_max) = sorted([nums[i], 
                                    nums[i] * cur_min, nums[i] * cur_max])
            result = max(result, cur_max)
        return result
                

if __name__ == "__main__":
    solution = Solution()
    print solution.maxProduct([2,3,-2,4])
    print solution.maxProduct([0, 2])
