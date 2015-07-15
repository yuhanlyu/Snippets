# Given a singly linked list L: L0 -> .. -> Ln
# reorder it to: L0 -> Ln -> L1 -> Ln-1 ...
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if not head: return head
        fast = slow = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow, prev = None, slow.next, None
        while slow:
            prev, slow.next, slow = slow, prev, slow.next
        while head and prev:
            prev.next,prev,head.next,head = head.next,prev.next,prev,head.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    solution.reorderList(head)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val
