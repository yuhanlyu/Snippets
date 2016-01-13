class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
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
