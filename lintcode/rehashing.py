"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        result = [None] * (2 * len(hashTable))
        last = [None] * (2 * len(hashTable))
        for node in hashTable:
            while node:
                next, node.next = node.next, None
                if not result[node.val % len(result)]:
                    result[node.val % len(result)] = node
                    last[node.val % len(result)] = node
                else:
                    last[node.val % len(result)].next = node
                    last[node.val % len(result)] = node
                node = next
        return result
