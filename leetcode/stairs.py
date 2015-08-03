# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top?
# Time Complexity: O(lg n)
# Space Complexity: O(1)

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        x, y, a, b = 1, 0, 1, 1
        while n > 0:
            if n & 1: x, y = a * x + b * y, b * x + y * (a - b)
            a, b, n = a * a + b * b, b * (2 * a - b), n >> 1
        return x
                
if __name__ == "__main__":
    solution = Solution()
    print solution.climbStairs(2)
    print solution.climbStairs(5)
    print solution.climbStairs(10)
