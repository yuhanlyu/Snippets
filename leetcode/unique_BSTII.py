# Given n, generate all structurally unique BST's (binary search trees) that 
# store values 1...n.
# Time Complexity: O(n4^n)
# Space Complexity: O(n4^n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {integer} n
    # @return {TreeNode[]}
    def generateTrees(self, n):
        if n == 0: return [[]]
        DP = [[[None] for _ in xrange(n + 2) ] for _ in xrange(n + 2)]
        for k in xrange(n):
            for i in xrange(1, n - k + 1):
                DP[i][i + k] = []
                for root in xrange(i, i + k + 1):
                    for left in DP[i][root - 1]:
                        for right in DP[root + 1][i + k]:
                            node = TreeNode(root)
                            node.left, node.right = left, right
                            DP[i][i + k].append(node)
        return DP[1][n]

if __name__ == "__main__":
    solution = Solution()
    for root in solution.generateTrees(3):
        print root.val
