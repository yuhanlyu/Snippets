# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice 
# in the array, and it should return false if every element is distinct.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        visited = set()
        for x in nums:
            if x in visited:
                return True 
            visited.add(x)
        return False

if __name__ == "__main__":
    solution = Solution()
    print solution.containsDuplicate([1,2,3])
