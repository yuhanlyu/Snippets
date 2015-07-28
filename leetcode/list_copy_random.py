# A linked list is given such that each node contains an additional random 
# pointer which could point to any node in the list or null.
# Return a deep copy of the list.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if not head: return None
        cur = head
        while cur:
            cur.next, next = RandomListNode(cur.label), cur.next
            cur.next.next, cur = next, next
        cur = head
        while cur:
            if cur.random: cur.next.random = cur.random.next
            cur = cur.next.next
        cur1, cur2, result = head, head.next, head.next
        while cur1:
            cur1.next = cur1.next.next 
            cur2.next = cur2.next.next if cur1.next else None
            cur1, cur2 = cur1.next, cur2.next
        return result

if __name__ == "__main__":
    solution = Solution()
    head = RandomListNode(0)
    head.next = RandomListNode(1)
    head.next.next = RandomListNode(2)
    head.random = head.next.next
    head = solution.copyRandomList(head)
    print head.random.label
