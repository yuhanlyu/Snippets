# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.
# Time complexity: O(n)
# Space complexity: O(output)

class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return M[num / 1000] + C[(num % 1000) / 100] + \
               X[(num % 100) / 10] + I[num % 10]

if __name__ == "__main__":
    solution = Solution()
    print solution.intToRoman(3999)
