# Given two numbers represented as strings, 
# return multiplication of the numbers as a string.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1, num2 = map(int, num1), map(int, num2)
        result = [0] * (len(num1) + len(num2))
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                result[~(i + j)] += num1[~i] * num2[~j]
        index = len(result) - 1
        for i in xrange(len(result) - 1, -1, -1):
            if result[i] >= 10:
                result[i - 1] += result[i] / 10
                result[i] %= 10
            if result[i] != 0: index = i
        return ''.join(str(result[i]) for i in xrange(index, len(result)))

if __name__ == "__main__":
    solution = Solution()
    print solution.multiply("0", "0")
