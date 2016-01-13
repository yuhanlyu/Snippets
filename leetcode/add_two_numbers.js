# You are given two linked lists representing two non-negative numbers. 
# The digits are stored in reverse order and each of their nodes contain 
# a single digit. Add the two numbers and return it as a linked list.
# Time Complexity: O(n)
# Space Complexity: O(1)
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var previous = l1, current = l1        
    for (var carry = 0; current && l2; current = current.next, l2 = l2.next) {
        var t = current.val + l2.val + carry
        carry = Math.floor(t / 10)
        current.val = t % 10
        previous = current
    }
    if (l2)
        current = previous.next = l2
    for (; current; current = current.next) {
        t = current.val + carry
        carry = Math.floor(t / 10)
        current.val = t % 10
        previous = current
    }
    if (carry)
        previous.next = new ListNode(carry)
    return l1;
};
