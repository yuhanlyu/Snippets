# Given an array S of n integers, are there elements a, b, c, and d in S 
# such that a + b + c + d = target? Find all unique quadruplets in the array 
# which gives the sum of target.

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        all_pairs = dict()
        for i in xrange(len(nums)):
            for j in xrange(i + 1, len(nums)):
                if nums[i] + nums[j] not in all_pairs:
                    all_pairs[nums[i] + nums[j]] = []
                all_pairs[nums[i] + nums[j]].append([i, j])
        solutions = set()
        for key, indices in all_pairs.iteritems():
            if target - key in all_pairs:
                solutions |= set((tuple(sorted([nums[i] for i in candidate])) \
                                  for candidate in \
                                  (index1 + index2 for index1 in indices \
                                      for index2 in all_pairs[target-key]) \
                                  if len(set(candidate)) == 4))
        return [list(solution) for solution in solutions]
                    
if __name__ == "__main__":
    solution = Solution()
    print solution.fourSum([1, 0, -1, 0, -2, 2], 0)
