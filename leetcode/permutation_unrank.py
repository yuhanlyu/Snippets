# Given n and k, return the kth permutation sequence.
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        fac, result = [1] * n, [i + 1 for i in xrange(n)]
        for i in xrange(2, n):
            fac[i] = fac[i - 1] * i
        k -= 1
        for i in xrange(n - 1):
            (d, k) = divmod(k, fac[n - i - 1])
            if d: result[i:i + d + 1] = [result[i + d]] + result[i:i + d]
        return ''.join([str(x) for x in result])

if __name__ == "__main__":
    solution = Solution()
    print solution.getPermutation(9, 5000)
    print solution.getPermutation(1, 1)
    print solution.getPermutation(2, 2)
    print solution.getPermutation(3, 6)
    print solution.getPermutation(4, 6)
