# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        current = dummy = ListNode(None)
        dummy.next = head
        while current.next and current.next.next:
            first, second = current.next, current.next.next
            current.next, first.next, second.next = second, second.next, first
            current = current.next.next
        return dummy.next
