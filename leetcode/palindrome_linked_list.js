/* Given a singly linked list, determine if it is a palindrome.
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
 * @return {boolean}
 */
var isPalindrome = function(head) {
    var slow = head, fast = head;
    for (var prev = null; fast && fast.next; ) {
        fast = fast.next.next;
        var temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    }
    if (fast)
        slow = slow.next;
    while (prev && prev.val === slow.val) {
        prev = prev.next;
        slow = slow.next;
    }
    return prev === null;
};
