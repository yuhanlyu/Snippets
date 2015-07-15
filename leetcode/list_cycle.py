# Given a linked list, determine if it has a cycle in it.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        slow = fast = head
        while fast:
            slow, fast = slow.next, fast.next
            if not fast: break
            fast = fast.next
            if slow == fast: return True
        return False

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node1
    solution = Solution()
    print solution.hasCycle(head)
