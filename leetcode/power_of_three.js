/* Given an integer, write a function to determine if it is a power of three.
 * Time Complexity: O(1)
 * Space Complexity: O(1)
 */

/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    return n > 0 && (1162261467 % n === 0);
};
