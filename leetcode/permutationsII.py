# Given a collection of numbers that might contain duplicates, 
# return all possible unique permutations.
# Time Complexity: O((n+1)!)
# Space Complexity: O((n+1)!)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        nums.sort()
        result = [list(nums)]
        while True:
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            if i < 0: break
            j = len(nums) - 1
            while nums[i] >= nums[j]: 
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            left, right = i + 1, len(nums) - 1
            nums[i + 1:] = nums[-1:i:-1]
            result.append(list(nums))
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.permuteUnique([1, 1, 2])
