/* Implement an iterator over a binary search tree (BST). 
 * Your iterator will be initialized with the root node of a BST.
 * Calling next() will return the next smallest number in the BST.
 * next() and hasNext() should run in average O(1) time and uses O(h) memory, 
 * where h is the height of the tree.
 * Time Complexity: O(n)
 * Space Complexity: O(h), h is the height of the tree, O(1) is doable by using
 * Morris traversal
 */

/**
 * Definition for binary tree
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @constructor
 * @param {TreeNode} root - root of the binary search tree
 */
var BSTIterator = function(root) {
    for (this.stack = []; root; root = root.left)
        this.stack.push(root);
};


/**
 * @this BSTIterator
 * @returns {boolean} - whether we have a next smallest number
 */
BSTIterator.prototype.hasNext = function() {
    return this.stack.length > 0;
};

/**
 * @this BSTIterator
 * @returns {number} - the next smallest number
 */
BSTIterator.prototype.next = function() {
    var node = this.stack.pop();
    for (var cur = node.right; cur; cur = cur.left)
        this.stack.push(cur);
    return node.val;
};

/**
 * Your BSTIterator will be called like this:
 * var i = new BSTIterator(root), a = [];
 * while (i.hasNext()) a.push(i.next());
*/
