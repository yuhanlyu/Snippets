class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if not nums: return []
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
