/* Reverse digits of an integer.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    var sign = x >= 0 ? 1 : -1   
    x = Math.abs(x)
    for (var result = 0; x > 0; x = Math.floor(x / 10))
        result = result * 10 + x % 10
    result *= sign
    return -2147483648 <= result && result <= 2147483647 ? result : 0
};
