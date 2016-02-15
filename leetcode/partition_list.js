/* Given a linked list and a value x, partition it such that all nodes less 
 * than x come before nodes greater than or equal to x.
 * You should preserve the original relative order of the nodes in each of 
 * the two partitions.
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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
    var tail = new ListNode(null), dummy = new ListNode(null)    
    var current = dummy.next = head
    for (var greater = tail, previous = dummy; current; current = current.next){
        if (current.val >= x) {
            tail.next = current
            tail = current
            previous.next = current.next
        } else 
            previous = current
    }
    tail.next = null
    previous.next = greater.next
    return dummy.next
};
