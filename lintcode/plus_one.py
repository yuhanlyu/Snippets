class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        for index in xrange(len(digits) - 1, -1, -1):
            if digits[index] != 9:
                digits[index] += 1
                return digits
            digits[index] = 0
        return [1] + digits
