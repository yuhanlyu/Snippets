# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        pre, cur = root, None
        while pre.left:
            cur = pre
            while cur:
                cur.left.next = cur.right
                if cur.next: cur.right.next = cur.next.left
                cur = cur.next
            pre = pre.left

if __name__ == "__main__":
    node = TreeLinkNode(2)
    node.left = TreeLinkNode(1)
    node.right = TreeLinkNode(3)
    solution = Solution()
    solution.connect(node)
    print node.left.next.val
