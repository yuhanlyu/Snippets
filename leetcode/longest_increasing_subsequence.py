# Given an unsorted array of integers, find the length of longest increasing 
# subsequence.
# Time Complexity: O(n lg n)
# Space Complexity: O(n)

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ends = [float('inf')] * (len(nums) + 1)
        for num in nums:
            ends[bisect.bisect_left(ends, num)] = num
        return ends.index(float('inf'))

if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
