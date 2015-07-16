# Given an array of n integers where n > 1, nums, return an array output such 
# that output[i] is equal to the product of all the elements of nums except 
# nums[i]. Solve it without division and in O(n).
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        result, result[0] = [0] * len(nums), 1
        for index in xrange(1, len(nums)):
            result[index] = nums[index - 1] * result[index - 1]
        product = 1
        for index in xrange(len(nums) - 1, -1, -1):
            result[index] *= product
            product *= nums[index]
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.productExceptSelf([1,2,3,4])
