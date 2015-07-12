# Given a sorted array, remove the duplicates in place such that 
# each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this 
# in place with constant memory.
# For example, given input array nums = [1,1,2],
# Your function should return length = 2, with the first two 
# elements of nums being 1 and 2 respectively. 
# It doesn't matter what you leave beyond the new length.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        current = 0
        for num in nums:
            if current == 0 or num > nums[current - 1]:
                nums[current] = num
                current += 1
        return current

if __name__ == "__main__":
    solution = Solution()
    print solution.removeDuplicates([1, 2, 2, 3, 3, 5, 6, 6, 7])
