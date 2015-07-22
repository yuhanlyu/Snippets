# Given a collection of integers that might contain duplicates, nums, 
# return all possible subsets.
# Time Complexity: O(n2^n)
# Space Complexity: O(n2^n)

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        cnt, result = {}, []
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        c, nums[:] = [0] * len(cnt), sorted(cnt.keys())
        while True:
            tmp = sum([[nums[i]] * c[i] for i in xrange(len(c))], [])
            result.append(tmp)
            j = 0
            while j < len(nums) and c[j] == cnt[nums[j]]:
                c[j] = 0
                j += 1
            if j == len(nums): break
            c[j] += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.subsetsWithDup([1, 2, 2])
