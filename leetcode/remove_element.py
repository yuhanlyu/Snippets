# Given an array and a value, remove all instances of that value in place 
# and return the new length.
# The order of elements can be changed. 
# It doesn't matter what you leave beyond the new length.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        current = 0
        for index in xrange(len(nums)):
            if nums[index] != val:
                nums[current] = nums[index]
                current += 1
        return current

if __name__ == "__main__":
    solution = Solution()
    print solution.removeElement([1, 2, 3, 2, 3], 1)
