/* Given a sorted linked list, delete all duplicates such that 
 * each element appear only once.
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
    if (!head) return null    
    for (var current = head; current.next; ) {
        if (current.val == current.next.val)
            current.next = current.next.next
        else
            current = current.next
    }
    return head
};
