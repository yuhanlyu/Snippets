# Given an array nums containing n + 1 integers where each integer is between 1 
# and n (inclusive), prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = nums[len(nums) - 1], nums[nums[len(nums) - 1] - 1]
        while slow != fast:
            slow, fast = nums[slow - 1], nums[nums[fast - 1] - 1]
        slow = len(nums)
        while slow != fast:
            slow, fast = nums[slow - 1], nums[fast - 1]
        return slow

if __name__ == "__main__":
    solution = Solution()
    print solution.findDuplicate([1, 1])
