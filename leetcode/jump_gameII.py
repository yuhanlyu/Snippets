# Given an array of non-negative integers, you are initially positioned at the 
# first index of the array.
# Each element in the array represents your maximum jump length at that 
# position.
# Your goal is to reach the last index in the minimum number of jumps.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        m, next, jump = 0, 0, 0
        for i in xrange(len(nums) - 1):
            next = max(next, i + nums[i])
            if i == m: jump, m = jump + 1, next
        return jump

if __name__ == "__main__":
    solution = Solution()
    print solution.jump([2,1])
    print solution.jump([2,3,1,1,4])
    print solution.jump([3,2,1,0,4])
