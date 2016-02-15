/* Reverse a singly linked list.
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
var reverseList = function(head) {
    for (var prev = null; head; ) {
        var temp = head.next
        head.next = prev
        prev = head
        head = temp
    }
    return prev
};
