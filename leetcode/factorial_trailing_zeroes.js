/* Given an integer n, return the number of trailing zeroes in n!.
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)

/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    for (var count = 0; n > 0; n = Math.floor(n / 5))
        count += Math.floor(n / 5)
    return count
};
