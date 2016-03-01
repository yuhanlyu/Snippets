/* Given a singly linked list, group all odd nodes together followed by the 
 * even nodes. Please note here we are talking about the node number and not 
 * the value in the nodes.
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
var oddEvenList = function(head) {
    if (head && head.next) {
        var even_head = head.next;
        for (var odd = head, even = even_head; even !== null && even.next !== null; ) {
            odd.next = odd.next.next; 
            even.next = even.next.next; 
            odd = odd.next;
            even = even.next;
        }
        odd.next = even_head; 
    }
    return head;
};
