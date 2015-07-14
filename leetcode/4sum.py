# Given an array S of n integers, are there elements a, b, c, and d in S 
# such that a + b + c + d = target? Find all unique quadruplets in the array 
# which gives the sum of target.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        all_pairs = {}
        nums.sort()
        for i, j in ((s, l) for l in xrange(len(nums)) for s in xrange(l)):
            all_pairs.setdefault(nums[i] + nums[j], []).append((i, j))
        return [list(solution) for solution in
          set(((nums[i], nums[j], nums[k], nums[l])
          for j in xrange(len(nums)) for i in xrange(j)
          for k, l in all_pairs.get(target - nums[i] - nums[j], []) if k > j))]
                    
if __name__ == "__main__":
    solution = Solution()
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
