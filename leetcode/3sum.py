# Given an array S of n integers, are there elements a, b, c in S such that 
# a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.
# Time Complexity: O(n^2)
# Space Complexity: O(output) assuming sorting in place

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        result = []
        nums.sort()
        for index in xrange(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            if index == 0 or nums[index] != nums[index-1]:
                while left < right:
                    if nums[index] + nums[left] + nums[right] == 0:
                        result.append([nums[index], nums[left], nums[right]])
                        while left < right and nums[left] == result[-1][1]:
                            left += 1
                        while left < right and nums[right] == result[-1][2]:
                            right -= 1
                    elif nums[index] + nums[left] + nums[right] < 0:
                        left += 1
                    else:
                        right -= 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.threeSum([-1, 0, 1, 2, -1, -4])
