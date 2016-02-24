class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        result, cur, begin, max_sum = [0, 0], 0, 0, -2 ** 32
        for i, num in enumerate(A):
            cur += num
            if cur > max_sum:
                max_sum = cur
                result = [begin, i]
            if cur < 0:
                cur = 0
                begin = i + 1
        return result
