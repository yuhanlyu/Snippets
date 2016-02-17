/* Implement int sqrt(int x).  Compute and return the square root of x.
 * Time Complexity: O(lg lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    for (var n = 1, nn = 3; Math.abs(n - nn) > 1; ) {
        nn = n
        n = Math.floor((n + Math.floor(x / n)) / 2)
    }
    return n * n <= x ? n : n - 1
};
