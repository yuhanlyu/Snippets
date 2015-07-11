# Given an array of integers, find two numbers such that they add up to a 
# specific target number.
# Time Complexity: O(n) in average
# Space Complexity: O(n)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        elements = {value : index for index, value in enumerate(nums)}
        for index, x in enumerate(nums):
            if target - x in elements and index != elements[target - x]:
                return [index + 1, elements[target - x] + 1]

if __name__ == "__main__":
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
    print solution.twoSum([3, 2, 4], 6)
