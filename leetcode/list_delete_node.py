# Write a function to delete a node (except the tail) in a singly linked list, 
# given only access to that node.
# Time Complexity: O(1)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val, node.next = node.next.val, node.next.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.deleteNode(head.next.next)
    print head.val, head.next.val, head.next.next.val
