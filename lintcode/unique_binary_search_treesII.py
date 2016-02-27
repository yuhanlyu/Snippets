"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        if n == 0: return [None]
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
