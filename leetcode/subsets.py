# Given a set of distinct integers, nums, return all possible subsets.
# Time Complexity: O(n2^n)
# Space Complexity: O(n2^n)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            for i in xrange(len(result)):
                result.append(result[i] + [num])
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.subsets([1, 2, 3])
