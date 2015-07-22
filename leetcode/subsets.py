# Given a set of distinct integers, nums, return all possible subsets.
# Time Complexity: O(n2^n)
# Space Complexity: O(n2^n)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if not nums: return []
        nums.sort()
        result, x, k = [[]], [0] * (len(nums)), 0
        while True:
            result.append([nums[i] for i in x[0:k + 1]])
            if x[k] == len(nums) - 1:
                if k == 0: break
                k -= 1
                x[k] += 1
            else:
                k += 1
                x[k] = x[k - 1] + 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.subsets([1, 2, 3])
