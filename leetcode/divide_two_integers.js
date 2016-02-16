/* Divide two integers without using multiplication, division and mod operator.
 * If it is overflow, return MAX_INT.
 * Time Complexity: O(lg n)
 * Space Complexity: O(1)
 */

/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
var divide = function(dividend, divisor) {
    var tmp = Math.abs(divisor), n = Math.abs(dividend)
    for (var shift = 0; tmp * 2 <= n; tmp *= 2)
        ++shift
    for (var ans = 0, d = Math.abs(divisor) ; d <= n; tmp = Math.floor(tmp / 2), --shift) {
        if (n >= tmp) {
            n -= tmp
            ans += Math.pow(2, shift)
        }
    }
    ans = dividend * divisor >= 0 ? ans : -ans
    return -2147483648 <= ans && ans <= 2147483647 ? ans : 2147483647
};
