# Given a range [m, n] where 0 <= m <= n <= 2147483647, 
# return the bitwise AND of all numbers in this range, inclusive.
# Time Complexity: O(lg W), W is the number of bits
# Space Complexity: O(1)

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def rangeBitwiseAnd(self, m, n):
        D = [0, 9, 1, 10, 13, 21, 2, 29, 11, 14, 16, 18, 22, 25, 3, 30,
             8, 12, 20, 28, 15, 17, 24, 7, 19, 27, 23, 6, 26, 5, 4, 31]
        v = m ^ n
        v |= v >> 1
        v |= v >> 2
        v |= v >> 4
        v |= v >> 8
        v |= v >> 16
        r = D[((v * 0x07C4ACDD) >> 27) & 0x1F]
        return (m >> r) << r

if __name__ == "__main__":
    solution = Solution()
    print solution.rangeBitwiseAnd(0x71, 0x77)
