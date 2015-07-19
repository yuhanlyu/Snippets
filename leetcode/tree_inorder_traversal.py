# Given a binary tree, return the inorder traversal of its nodes' values.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        result, node = [], root
        while node:
            if node.left:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right:
                    result.append(node.val)
                    node, pre.right = node.right, None
                else:
                    pre.right, node = node, node.left
            else:
                result.append(node.val)
                node = node.right
        return result

#class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
#    def inorderTraversal(self, root):
#        stack, result, node = [], [], root
#        while stack or node:
#            if node:
#                stack.append(node)
#                node = node.left
#            else:
#                node = stack.pop()
#                result.append(node.val)
#                node = node.right
#        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    solution = Solution()
    print solution.inorderTraversal(root)
