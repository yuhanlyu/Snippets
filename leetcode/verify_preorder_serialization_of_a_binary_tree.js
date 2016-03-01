/* Given a string of comma separated values, verify whether it is a correct 
 * preorder traversal serialization of a binary tree. Find an algorithm 
 * without reconstructing the tree.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */


/**
 * @param {string} preorder
 * @return {boolean}
 */
var isValidSerialization = function(preorder) {
    var need = 1;
    for (var val of preorder.split(",")) {
        if (need === 0)
            return false;
        need -= " #".indexOf(val);
    }
    return need === 0;
};
