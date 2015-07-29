# A peak element is an element that is greater than its neighbors.
# Given an input array where num[i] != num[i+1], find a peak element and return 
# its index.
# The array may contain multiple peaks, in that case return the index to any 
# one of the peaks is fine.
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == "__main__":
    solution = Solution()
    print solution.findPeakElement([1, 2, 3, 1])
