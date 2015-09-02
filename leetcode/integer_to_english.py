# Convert a non-negative integer to its english words representation. 
# Given input is guaranteed to be less than 2^31 - 1.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        def helper(num):
            below19 = ["", "One", "Two", "Three", "Four", "Five", 
                       "Six", "Seven", "Eight", "Nine", "Ten", 
                       "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", 
                       "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
            tens = ["", "",  "Twenty", "Thirty", "Forty", "Fifty", 
                    "Sixty", "Seventy", "Eighty", "Ninety"]
            if num < 20:
                return [below19[num]] if num else []
            if num < 100:
                return [tens[num / 10]] + helper(num % 10)
            if num < 1000:
                return [below19[num / 100], "Hundred"] + helper(num % 100)
            for p, w in enumerate(("Thousand", "Million", "Billion"), 1):
                if num < 1000**(p + 1):
                    return helper(num / 1000**p ) + [w] + helper(num % 1000**p)
        return ' '.join(helper(num)) if num else "Zero"


if __name__ == "__main__":
    solution = Solution()
    print solution.numberToWords(123)
    print solution.numberToWords(12345)
    print solution.numberToWords(1234567)
