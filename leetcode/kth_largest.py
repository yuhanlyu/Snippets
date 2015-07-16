# Kth Largest Element in an Array 
# Time Complexity: O(n) in average
# Space Complexity: O(n) (this can be reduced to O(1) by in-place partition)
# O(n + k lg n ) solution
# return heapq.nlargest(k, nums)[-1]

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        while True:
            larger = [num for num in nums if num > nums[0]]
            eq = nums.count(nums[0])
            if len(larger) < k <= len(larger) + eq:
                return nums[0]
            if len(larger) >= k:
                nums = larger
            else:
                k -= len(larger) + eq
                nums = [num for num in nums if num < nums[0]]

if __name__ == "__main__":
    solution = Solution()
    print solution.findKthLargest([3,2,1,5,6,4], 2)
