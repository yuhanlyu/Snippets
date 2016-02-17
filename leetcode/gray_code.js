/* Given a non-negative integer n representing the total number of bits in 
 * the code, print the sequence of gray code. 
 * A gray code sequence must begin with 0.
 * Time Complexity: O(2^n)
 * Space Complexity: O(2^n)
 */

/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    var result = []
    for (var x = 0; x < Math.pow(2, n); ++x)
        result.push((x >> 1) ^ x)
    return result
};
