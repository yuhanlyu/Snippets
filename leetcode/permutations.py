# Given a collection of numbers, return all possible permutations.
# Time Complexity: O((n+1)!)
# Space Complexity: O((n+1)!)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        c, result, i = [0] * len(nums), [list(nums)], 1
        while i < len(nums):
            if c[i] == i:
                c[i], i = 0, i + 1
            else:
                nums[(i % 2) * c[i]], nums[i] = nums[i], nums[(i % 2) * c[i]]
                result.append(list(nums))
                c[i] += 1
                i = 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.permute([1, 2, 3])
