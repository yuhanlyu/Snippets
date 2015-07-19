# Follow up for problem "Populating Next Right Pointers in Each Node".
# What if the given tree could be any binary tree? 
# Would your previous solution still work?
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
        dummy, dummy.next = TreeLinkNode(0), root
        while dummy.next:
            tail, cur, dummy.next = dummy, dummy.next, None
            while cur:
                if cur.left:
                    tail.next, tail = cur.left, cur.left
                if cur.right:
                    tail.next, tail = cur.right, cur.right
                cur = cur.next

if __name__ == "__main__":
    node = TreeLinkNode(2)
    node.left = TreeLinkNode(1)
    node.right = TreeLinkNode(3)
    solution = Solution()
    solution.connect(node)
    print node.left.next.val
