# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number
# on it represented by array nums. You are asked to burst all the balloons. 
# If the you burst balloon i you will get nums[left] * nums[i] * nums[right] 
# coins. Here left and right are adjacent indices of i. After the burst, the 
# left and right then becomes adjacent.
# Find the maximum coins you can collect by bursting the balloons wisely.
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        F = [[0] * len(nums) for _ in xrange(len(nums))]
        for size in xrange(2, len(nums)):
            for i in xrange(len(nums) - size):
                j = i + size
                for k in xrange(i + 1, j):
                    F[i][j] = max(F[i][j], \
                          nums[i] * nums[k] * nums[j] + F[i][k] + F[k][j])
        return F[0][-1]

if __name__ == "__main__":
    solution = Solution()
    print solution.maxCoins([3, 1, 5, 8])
