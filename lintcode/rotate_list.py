# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        if not head: return head
        count, current = 1, head
        while current.next:
            current = current.next
            count += 1
        current.next = head
        for _ in xrange(count - k % count):
            current = current.next
        head, current.next = current.next, None
        return head
