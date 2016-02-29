# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        cur = dummy = ListNode(0)
        dummy.next = head
        while cur.next:
            g_head, i = cur, 0
            while i < k:
                if g_head.next: g_head, i = g_head.next, i + 1
                else: break
            if i != k: break
            g_head, prev, next = cur.next, g_head.next, g_head.next
            while g_head != next:
                prev, g_head.next, g_head = g_head, prev, g_head.next
            cur.next, cur = prev, cur.next
        return dummy.next
