# Given an array of non-negative integers, you are initially positioned at the 
# first index of the array.
# Each element in the array represents your maximum jump length at that 
# position.
# Determine if you are able to reach the last index.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        i = m = 0
        while i < len(nums) and i <= m:
            m = max(m, i + nums[i])
            i += 1
        return i == len(nums)

if __name__ == "__main__":
    solution = Solution()
    print solution.canJump([2,3,1,1,4])
    print solution.canJump([3,2,1,0,4])
