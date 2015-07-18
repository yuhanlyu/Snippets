# Kth Largest Element in an Array 
# Time Complexity: O(n) in average
# Space Complexity: O(1)
# O(n + k lg n ) solution
# return heapq.nlargest(k, nums)[-1]

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        while True:
            larger = sum(num > nums[0] for num in nums)
            eq = nums.count(nums[0])
            if larger < k <= larger + eq:
                return nums[0]
            if larger >= k:
                nums[:] = (num for num in nums if num > nums[0])
            else:
                k -= larger + eq
                nums[:] = (num for num in nums if num < nums[0])

if __name__ == "__main__":
    solution = Solution()
    print solution.findKthLargest([3,2,1,5,6,4], 2)
