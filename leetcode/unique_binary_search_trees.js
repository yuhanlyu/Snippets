/* Given n, how many structurally unique BST's (binary search trees) 
 * that store values 1...n?
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    for (var C = 1, i = 1; i < n; ++i)
        C = (C * (4 * i + 2)) / (i + 2)
    return C
};
