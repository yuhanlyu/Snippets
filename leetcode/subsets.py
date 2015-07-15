# Given a set of distinct integers, nums, return all possible subsets.
# Time Complexity: O(2^n)
# Space Complexity: O(n2^n)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        return reduce(lambda z, x: z + [y + [x] for y in z], sorted(nums), [[]])

if __name__ == "__main__":
    solution = Solution()
    print solution.subsets([0])
