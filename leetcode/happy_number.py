# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: 
# Starting with any positive integer, replace the number by the sum of the 
# squares of its digits, and repeat the process until the number equals 1 
# (where it will stay), or it loops endlessly in a cycle which does not 
# include 1. Those numbers for which this process ends in 1 are happy numbers.
# Space Complexity: O(1)

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        def sum_of_square(n):
            result = 0
            while n > 0:
                n, remainder = divmod(n, 10)
                result += remainder * remainder
            return result
        slow, fast = sum_of_square(n), sum_of_square(sum_of_square(n))
        while slow != fast:
            slow, fast = sum_of_square(slow), sum_of_square(sum_of_square(fast))
        return True if fast == 1 else False

if __name__ == "__main__":
    solution = Solution()
    print [x for x in xrange(500) if solution.isHappy(x)][:8]
    print "[1, 7, 10, 13, 19, 23, 28, 31] is the correct answer"
