# Given an array nums, write a function to move all 0's to the end of it while 
# maintaining the relative order of the non-zero elements.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cur = 0
        for i in xrange(len(nums)):
            if nums[i]:
                if nums[i] != nums[cur]:
                    nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1

if __name__ == "__main__":
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print nums
