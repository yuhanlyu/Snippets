# Given a non-negative number represented as an array of digits, 
# plus one to the number.
# The digits are stored such that the most significant digit is at the 
# head of the list.
# Time complexity: O(n)
# Space complexity: O(1), if the lengths of input and output are the same

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        for index in xrange(len(digits) - 1, -1, -1):
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                return digits
        digits.insert(0, 1)
        return digits

if __name__ == "__main__":
    solution = Solution()
    print solution.plusOne([9, 9, 9])
