/* Write a function that takes an unsigned integer and 
 * returns the number of '1' bits it has (also known as the Hamming weight).
 * Time Complexity: O(lg n), n is the number of bits
 * Space Complexity: O(1)
 */

/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    n -= ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    return (((n + (n >> 4) & 0x0F0F0F0F) * 0x01010101) & 0xFFFFFFFF) >> 24
};
