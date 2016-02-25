/* Given a sorted linked list, delete all nodes that have duplicate numbers, 
 * leaving only distinct numbers from the original list.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    if (!head)
        return null;
    var dummy = new ListNode(null);
    dummy.next = head;
    for (var current = dummy; current.next && current.next.next; ) {
        if (current.next.val === current.next.next.val) {
            for (var v = current.next.val; current.next && current.next.val === v; )
                current.next = current.next.next;
        } else
            current = current.next;
    }
    return dummy.next;
};
