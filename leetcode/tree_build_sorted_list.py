# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.
# Time Complexity: O(n)
# Space Complexity: O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        def helper(head, count):
            if not count: return None, head
            (l, tail) = helper(head, count / 2)
            root = TreeNode(tail.val)
            (r, tail) = helper(tail.next, count - count / 2 - 1)
            root.left, root.right = l, r
            return root, tail
        cur, length = head, 0
        while cur:
            length += 1
            cur = cur.next
        return helper(head, length)[0]

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    solution = Solution()
    node = solution.sortedListToBST(head)
    print node.val, node.left.val, node.right.val
