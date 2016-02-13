"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        def helper(root, path, result):
            if not root.left and not root.right:
                result.append("->".join(path + [str(root.val)]))
            else:
                if root.left: helper(root.left, path + [str(root.val)], result)
                if root.right: helper(root.right, path+[str(root.val)], result)
            return result
        return helper(root, [], []) if root else []
