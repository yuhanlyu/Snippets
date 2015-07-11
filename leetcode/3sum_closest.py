# Given an array S of n integers, find three integers in S such that the sum 
# is closest to a given number, target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for index in xrange(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left < right:
                sum = nums[index] + nums[left] + nums[right]
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum <= target:
                    left += 1
                else:
                    right -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.threeSumClosest([-1, 2, 1, -4], 1)
