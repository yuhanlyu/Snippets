/* Given a singly linked list where elements are sorted in ascending order, 
 * convert it to a height balanced BST.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    function helper(head, count) {
        if (count === 0)
            return [null, head];
        var left = helper(head, Math.floor(count / 2));
        var root = new TreeNode(left[1].val);
        var right = helper(left[1].next, count - 1 - Math.floor(count / 2));
        root.left = left[0];
        root.right = right[0];
        return [root, right[1]];
    }
    for (var cur = head, length = 0; cur; ++length)
        cur = cur.next;
    return helper(head, length)[0];
};
