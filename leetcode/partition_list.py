# Given a linked list and a value x, partition it such that all nodes less 
# than x come before nodes greater than or equal to x.
# You should preserve the original relative order of the nodes in each of 
# the two partitions.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        tail = greater = ListNode(None)
        previous = dummy = ListNode(None)
        current = dummy.next = head
        while current:
            if current.val >= x:
                tail.next, tail = current, current
                previous.next = current.next
            else:
                previous = current
            current = current.next
        tail.next = None
        previous.next = greater.next
        return dummy.next
        

if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    head = solution.partition(head, 3)
    print head.val, head.next.val, head.next.next.val, head.next.next.next.val
