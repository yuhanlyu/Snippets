# Reverse a singly linked list.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            prev, head.next, head = head, prev, head.next
        return prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(6)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)
    solution = Solution()
    head = solution.reverseList(head)
    print head.val, head.next.val, head.next.next.val
