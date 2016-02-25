/* Given a singly linked list L0 -> L1 ...
 * Reorder to L0 -> Ln ...
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
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
    if (!head)
        return;
    for (var fast = head, slow = head; fast && fast.next; ) {
        slow = slow.next;
        fast = fast.next.next;
    }
    var temp = slow.next;
    slow.next = null;
    slow = temp;
    for (var prev = null; slow;) {
        temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    while (head && prev) {
        var temp1 = prev.next;
        var temp2 = head.next;
        prev.next = head.next;
        head.next = prev;
        prev = temp1;
        head = temp2;
    }
};
