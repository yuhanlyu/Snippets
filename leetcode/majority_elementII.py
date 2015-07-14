# Given an integer array of size n, find all elements that appear more than n/3 # times.
# Time complexity: O(n) in average
# Space complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        K = {}
        for num in nums:
            K[num] = K.get(num, 0) + 1
            if len(K) >= 3:
                K = dict([(a, c - 1) for (a, c) in K.iteritems() if c > 1])
        return [num for num in K if nums.count(num) > len(nums) / 3]

if __name__ == "__main__":
    solution = Solution()
    print solution.majorityElement([1, 2, 3, 4])
    print solution.majorityElement([1, 1, 1, 2, 2, 2, 3, 3, 3, 1])
