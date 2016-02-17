/* Given an integer, write a function to determine if it is a power of two.
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    return ((n & (n-1)) === 0) && (n > 0) ? true : false
};
