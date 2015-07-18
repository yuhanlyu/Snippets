# Given a binary tree, return the postorder traversal of its nodes' values.
# Time Complexity: O(n)
# Space Complexity: O(h), h is the height of the tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        stack, prev, result = [root] if root else [], root, []
        while stack:
            children = [x for x in (stack[-1].right, stack[-1].left) if x]
            if not children or prev in children:
                result.append(stack[-1].val)
                prev = stack.pop()
            else:
                stack.extend(children)
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.left = TreeNode(3)
    solution = Solution()
    print solution.postorderTraversal(root)
