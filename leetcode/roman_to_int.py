# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
# Time complexity: O(n) in average (O(n) worst can be achieved by perfect hash)
# Space complexity: O(1)

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        previous = result = map[s[-1]]
        for index in xrange(len(s) - 2, -1, -1):
            val = map[s[index]]
            result += val if val >= previous else -val
            previous = val
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.romanToInt("MMMCMXCIX")
