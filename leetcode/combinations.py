# Given two integers n and k, return all possible combinations of k numbers 
# out of 1 ... n.
# Time Complexity: O(n^k)
# Space Complexity: O(n^k)

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        result, x = [], (1 << k) - 1
        while x < (1 << n):
            result.append([i + 1 for i in xrange(n) if ((x >> i) & 1)])
            u = x & -x
            v = u + x
            x = v | (((v^x) / u) >> 2)
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.combine(4, 2)
