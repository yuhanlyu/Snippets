# Given an unsorted array of integers, find the length of the longest 
# consecutive elements sequence.
# Time Complexity: O(n) in average
# Space Complexity: O(n)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        b, result = {}, 0
        for num in nums:
            if num not in b:
                left, right = b.get(num - 1, num), b.get(num + 1, num)
                result = max(result, right - left + 1)
                b[num], b[left], b[right] = num, right, left
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.longestConsecutive([100, 4, 200, 1, 3, 2])
