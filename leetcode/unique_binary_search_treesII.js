/* Given n, generate all structurally unique BST's (binary search trees) that 
 * store values 1...n.
 * Time Complexity: O(n4^n)
 * Space Complexity: O(n4^n)
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
var generateTrees = function(n) {
    if (n === 0)
        return [];
    var DP = new Array(n + 2);
    for (var i = 0; i < DP.length; ++i) {
        for (var temp = new Array(n + 2), j = 0; j < n + 2; ++j) 
            temp[j] = [null];
        DP[i] = temp;
    }
    for (var k = 0; k < n; ++k) {
        for (i = 1; i < n - k + 1; ++i) {
            DP[i][i + k] = [];
            for (var root = i; root < i + k + 1; ++root) {
                for (var left of DP[i][root - 1]) {
                    for (var right of DP[root + 1][i + k]) {
                        var node = new TreeNode(root);
                        node.left = left;
                        node.right = right;
                        DP[i][i + k].push(node);
                    }
                }
            }
        }
    }
    return DP[1][n];
};
