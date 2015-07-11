# Given an array S of n integers, are there elements a, b, c, and d in S 
# such that a + b + c + d = target? Find all unique quadruplets in the array 
# which gives the sum of target.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        all_pairs, solutions = {}, set()
        nums.sort()
        for j, i in ((a, b) for a in xrange(len(nums)) for b in xrange(a)):
            if nums[i] + nums[j] not in all_pairs:
                all_pairs[nums[i] + nums[j]] = []
            all_pairs[nums[i] + nums[j]].append((i, j))
        for j, i in ((a, b) for a in xrange(len(nums)) for b in xrange(a)):
            key = target - nums[i] - nums[j]
            if key in all_pairs:
                solutions |= set(((nums[i], nums[j], nums[k], nums[l])
                                   for k, l in all_pairs[key] if k > j))
        return [list(solution) for solution in solutions]
                    
if __name__ == "__main__":
    solution = Solution()
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
