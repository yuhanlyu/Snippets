# Implement next permutation, which rearranges numbers into the 
# lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest 
# possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        pivot = len(nums) - 1
        while pivot > 0 and nums[pivot - 1] >= nums[pivot]:
            pivot = pivot - 1
        if pivot == 0:
            nums.reverse()
        else:
            num, index = nums[pivot - 1], len(nums) - 1
            while nums[index] <= num:
                index = index - 1
            nums[index], nums[pivot - 1] = nums[pivot - 1], nums[index]
            for i in xrange((len(nums) - pivot) / 2):
                nums[pivot + i], nums[~i] = nums[~i], nums[pivot + i]

if __name__ == "__main__":
    solution = Solution()
    list = [1, 2, 3]
    solution.nextPermutation(list)
    print list
    list = [3, 2, 1]
    solution.nextPermutation(list)
    print list
    list = [1, 1, 5]
    solution.nextPermutation(list)
    print list
