# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than n/2 times.
# You may assume that the array is non-empty and 
# the majority element always exist in the array.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        count = 0
        for x in nums:
            if count == 0:
                candidate, count = x, 1
            else:
                count += (1 if x == candidate else -1)
        return candidate
            

if __name__ == "__main__":
    solution = Solution()
    print solution.majorityElement([1, 3, 3, 1, 1, 2, 3, 3, 1, 1, 1])
