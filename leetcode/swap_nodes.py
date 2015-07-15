# Given a linked list, swap every two adjacent nodes and return its head.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        current = dummy = ListNode(None)
        dummy.next = head
        while current.next and current.next.next:
            first, second = current.next, current.next.next
            current.next, first.next, second.next = second, second.next, first
            current = current.next.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution = Solution()
    head = solution.swapPairs(head)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val
