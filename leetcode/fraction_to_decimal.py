# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in 
# parentheses.
# Time Complexity: O(output)
# Space Complexity: O(output)

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        def factor(num, f):
            count = 0
            while num % f == 0:
                count += 1
                num /= f
            return (num, count)
        def generate(numerator, denominator, length, result):
            for _ in xrange(length):
                digit, numerator = divmod(numerator * 10, denominator)
                result.append(str(digit))
                if numerator == 0:
                    break
            return numerator
        result = [] if numerator * denominator >= 0 else ["-"]
        denominator = abs(denominator)
        n, numerator = divmod(abs(numerator), denominator)
        result.append(str(n))
        if numerator == 0: return ''.join(result)
        result.append(".")
        two_factor, five_factor, remain = 0, 0, denominator
        remain, two_factor = factor(denominator, 2)
        remain, five_factor = factor(remain, 5)
        numerator = generate(numerator, denominator, 
                             max(two_factor, five_factor), result)
        if remain != 1:
            length_period, a = 1, 10 % remain
            while a != 1:
                length_period += 1
                a = (a * 10) % remain
            result.append("(")
            generate(numerator, denominator, length_period, result)
            result.append(")")
        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    print solution.fractionToDecimal(1, 2)
    print solution.fractionToDecimal(2, 1)
    print solution.fractionToDecimal(2, 3)
    print solution.fractionToDecimal(1, 28)
    print solution.fractionToDecimal(50, 8)
    print solution.fractionToDecimal(7, -12)
