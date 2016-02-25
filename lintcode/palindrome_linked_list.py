# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast, prev, prev.next, slow = fast.next.next, slow, prev, slow.next
        if fast: slow = slow.next
        while prev and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        return not prev
