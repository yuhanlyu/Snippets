# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1...n?
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        C, C[0] = [0] * (n + 1), 1
        for i in xrange(1, n + 1):
            for j in xrange(0, i):
                C[i] += C[j] * C[i - j - 1]
        return C[n]

if __name__ == "__main__":
    solution = Solution()
    print solution.numTrees(3)
