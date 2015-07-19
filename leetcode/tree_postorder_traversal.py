# Given a binary tree, return the postorder traversal of its nodes' values.
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
    def postorderTraversal(self, root):
        def reverse(start, end):
            cur, next = start, start.right
            while cur != end:
                next.right, cur, next = cur, next, next.right
        result, prev, dummy, dummy.left = [], None, TreeNode(None), root
        node = dummy
        while node:
            if node.left:
                pre = node.left
                while pre.right and pre.right != node:
                    pre = pre.right
                if pre.right:
                    reverse(node.left, pre)
                    cur = pre
                    while True:
                        result.append(cur.val)
                        if cur == node.left: break
                        cur = cur.right
                    reverse(pre, node.left)
                    node, pre.right = node.right, None
                else:
                    node, pre.right = node.left, node
            else:
                node = node.right
        return result

#class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
#    def postorderTraversal(self, root):
#        stack, prev, result = [root] if root else [], root, []
#        while stack:
#            children = [x for x in (stack[-1].right, stack[-1].left) if x]
#            if not children or prev in children:
#                result.append(stack[-1].val)
#                prev = stack.pop()
#            else:
#                stack.extend(children)
#        return result


if __name__ == "__main__":
    #root = TreeNode(1)
    #root.right = TreeNode(2)
    #root.left = TreeNode(3)
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(1)
    solution = Solution()
    print solution.postorderTraversal(root)
