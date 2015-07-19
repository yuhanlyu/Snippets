# Given a binary tree and a sum, determine if the tree has a root-to-leaf 
# path such that adding up all the values along the path equals the given sum.
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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        result, node, current = False, root, 0
        while node:
            if node.left:
                pre = node.left
                count = pre.val
                while pre.right and pre.right != node:
                    pre = pre.right
                    count += pre.val
                if pre.right:
                    print count
                    node, pre.right = node.right, None
                    current -= count
                else:
                    current += node.val
                    pre.right, node = node, node.left
            else:
                current += node.val
                if not node.right:
                    if current == sum:
                        result = True
                else:
                    pre = node.right.left
                    while pre and pre != node:
                        pre = pre.right
                    if pre and current == sum:
                        result = True
                node = node.right
        return result

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    solution = Solution()
    print solution.hasPathSum(root, 22)
