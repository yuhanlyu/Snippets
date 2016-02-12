"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        dummy = ListNode(0, head)
        pre, cur = dummy, head
        while cur:
            if cur.next and cur.next.val < cur.val:
                while pre.next and pre.next.val < cur.next.val:
                    pre = pre.next
                pre.next, cur.next, pre.next.next, pre = \
                    cur.next, cur.next.next, pre.next, dummy
            else:
                cur = cur.next
        return dummy.next
