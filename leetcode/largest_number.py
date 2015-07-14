# Given a list of non negative integers, arrange them such that 
# they form the largest number.
# Time Complexity: O(n lg n)
# Space Complexity: O(n)

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        return ''.join(sorted([str(num) for num in nums],
                  cmp = lambda x, y: cmp(y + x, x + y))).lstrip('0') or '0'

if __name__ == "__main__":
    solution = Solution()
    print solution.largestNumber([3, 30, 34, 5, 9])
    print solution.largestNumber([0, 0])
