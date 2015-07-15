# Reverse a linked list from position m to n. Do it in-place and in one-pass.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        dummy = ListNode(None)
        dummy.next, before = head, dummy
        for _ in xrange(m - 1):
            before = before.next
        begin, after = before.next, before.next.next
        for _ in xrange(n - m):
            begin.next, after.next, before.next = after.next, before.next, after
            after = begin.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    head = solution.reverseBetween(head, 2, 4)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val
