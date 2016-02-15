/* Given two binary strings, return their sum (also a binary string).
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    for (var c = 0, aindex = a.length - 1, bindex = b.length - 1, result = [];
         aindex >= 0 || bindex >= 0 || c;
         --aindex, --bindex) {
        if (aindex >= 0)
            c += parseInt(a[aindex])
        if (bindex >= 0)
            c += parseInt(b[bindex])
        var remainder = c % 2
        c = Math.floor(c / 2)
        result.push(remainder.toString())
    }
    return result.reverse().join("")
};
