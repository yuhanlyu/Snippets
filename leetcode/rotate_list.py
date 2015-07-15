# Given a list, rotate the list to the right by k places, 
# where k is non-negative.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if not head: return []
        count, current = 1, head
        while current.next:
            current = current.next
            count += 1
        current.next = head
        for _ in xrange(count - k % count):
            current = current.next
        head, current.next = current.next, None
        return head

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    solution = Solution()
    head = solution.rotateRight(head, 2)
    print head.val, head.next.val, head.next.next.val
    #print head.val, head.next
