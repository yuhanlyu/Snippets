/* Implement atoi to convert a string to an integer.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {string} str
 * @return {number}
 */
var myAtoi = function(str) {
    var INT_MAX = 2147483647, INT_MIN = -2147483648, THRESHOLD = 214748364;
    for (var sign = 1, index = 0; index < str.length && str.charAt(index) === ' '; ++index)
        ;
    if (index < str.length && "+-".indexOf(str.charAt(index)) !== -1)
        sign = str.charAt(index++) === '+' ? 1 : -1;
    for (var result = 0; index < str.length; ++index) {
        var c = parseInt(str.charAt(index));
        if (isNaN(c))
            break;
        if (result > THRESHOLD || (result === THRESHOLD && c > 7))
            return sign === 1 ? INT_MAX : INT_MIN;
        result = result * 10 + c;
    }
    return result * sign;
};
