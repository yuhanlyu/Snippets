# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = fast = head
        while fast:
            slow, fast = slow.next, fast.next
            if not fast: break
            fast = fast.next
            if slow == fast: break
        if not fast: return None
        while head != slow:
            head, slow = head.next, slow.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    head.next = node1
    node1.next = node2
    node2.next = node1
    solution = Solution()
    print solution.detectCycle(head).val
