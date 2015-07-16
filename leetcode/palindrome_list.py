# Given a singly linked list, determine if it is a palindrome.
# Time Complexity: O(n)
# Space Complexity: O(1)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast, prev, prev.next, slow = fast.next.next, slow, prev, slow.next
        if fast: slow = slow.next
        while prev and prev.val == slow.val:
            prev, slow = prev.next, slow.next
        return not prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)
    solution = Solution()
    print solution.isPalindrome(head)
