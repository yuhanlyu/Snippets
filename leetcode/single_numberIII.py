# Given an array of numbers nums, in which exactly two elements appear only 
# once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        xor, ans = 0, 0
        for num in nums:
            xor ^= num
        for num in nums:
            if xor & -xor & num:
                ans ^= num
        return [xor ^ ans, ans]

if __name__ == "__main__":
    solution = Solution()
    print solution.singleNumber([1, 2, 1, 3, 2, 5])
