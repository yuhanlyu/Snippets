# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        current = 0
        for num in nums:
            if current < 2 or num > nums[current - 2]:
                nums[current] = num
                current += 1
        return current

if __name__ == "__main__":
    solution = Solution()
    print solution.removeDuplicates([1,1,1,2,2,3])
