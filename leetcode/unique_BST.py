# Given n, how many structurally unique BST's (binary search trees) 
# that store values 1...n?
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        C = 1
        for i in xrange(1, n):
            C = (C * (4 * i + 2)) / (i + 2)
        return C

if __name__ == "__main__":
    solution = Solution()
    print solution.numTrees(4)
