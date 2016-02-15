/* Merge two sorted linked lists and return it as a new list. 
 * The new list should be made by splicing together the nodes of the first 
 * two lists.
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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    dummy = new ListNode(0)    
    for (var current = dummy; l1 && l2; current = current.next) {
        if (l1.val <= l2.val) {
            current.next = l1
            l1 = l1.next
        } else {
            current.next = l2
            l2 = l2.next
        }
    }
    current.next = l1 ? l1 : l2
    return dummy.next
};
