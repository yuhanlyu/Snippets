# Rotate an array of n elements to the right by k steps.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        def reverse(nums, begin, end):
            while begin < end:
                nums[begin], nums[end] = nums[end], nums[begin]
                begin += 1
                end -= 1
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

if __name__ == "__main__":
    solution = Solution()
    print solution.rotate([1, 2], 3)
