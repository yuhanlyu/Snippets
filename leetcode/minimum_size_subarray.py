# Given an array of n positive integers and a positive integer s, find the 
# minimal length of a subarray of which the sum >= s. If there isn't one, 
# return 0 instead.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        result, begin, sum = None, 0, 0
        for i, num in enumerate(nums):
            sum += num
            while sum >= s:
                if not result or i - begin + 1 < result: result = i - begin + 1
                sum -= nums[begin]
                begin += 1
        return result if result else 0

if __name__ == "__main__":
    solution = Solution()
    print solution.minSubArrayLen(7, [2,3,1,2,4,3])
