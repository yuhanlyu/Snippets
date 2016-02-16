/* Implement pow(x, n).
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if (n < 0) {
        n = -n
        x = 1.0 / x
    }
    for (var result = 1; n > 0; n /= 2, x *= x) {
        if (n & 1)
            result *= x
    }
    return result
};
