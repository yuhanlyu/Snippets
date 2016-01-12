class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addTwoNumbers(self, l1, l2):
        carry, previous, current = 0, l1, l1
        while current and l2:
            carry, current.val = divmod(current.val + l2.val + carry, 10)
            previous, current, l2 = current, current.next, l2.next
        if l2: current = previous.next = l2
        while current:
            carry, current.val = divmod(current.val + carry, 10)
            previous, current = current, current.next
        if carry: previous.next = ListNode(carry)
        return l1

if __name__ == "__main__":
    list1 = ListNode(2)
    list1.next = ListNode(4)
    list1.next.next = ListNode(3)
    list2 = ListNode(5)
    list2.next = ListNode(6)
    list2.next.next = ListNode(4)
    solution = Solution()
    list = solution.addTwoNumbers(list1, list2)
    print list.val, list.next.val, list.next.next.val
