/* Remove all elements from a linked list of integers that have value val.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
var removeElements = function(head, val) {
    var dummy = new ListNode(0)
    dummy.next = head
    var current = dummy
    while (current.next) {
        if (current.next.val == val)
            current.next = current.next.next
        else
            current = current.next
    }
    return dummy.next
};
