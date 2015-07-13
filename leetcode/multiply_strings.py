# Given two numbers represented as strings, 
# return multiplication of the numbers as a string.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        result = [0] * (len(num1) + len(num2))
        num1, num2, begin = map(int, num1), map(int, num2), len(result) - 1
        for k in xrange(len(result)):
            for i in xrange(max(0, k + 1 - len(num2)), min(len(num1), k + 1)):
                result[~k] += num1[~i] * num2[~(k - i)]
            if result[~k] >= 10:
                result[~(k + 1)], result[~k] = divmod(result[~k], 10)
            if result[~k] != 0: begin = len(result) - k - 1
        return ''.join(str(result[i]) for i in xrange(begin, len(result)))

if __name__ == "__main__":
    solution = Solution()
    print solution.multiply("0", "0")
    print solution.multiply("1", "1")
