/* Given an integer, convert it to a roman numeral.
 * Input is guaranteed to be within the range from 1 to 3999.
 * Time complexity: O(n)
 * Space complexity: O(output)
 */

/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    var M = ["", "M", "MM", "MMM"];
    var C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
    var X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
    var I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
    var iM = Math.floor(num / 1000);
    var iC = Math.floor((num % 1000) / 100);
    var iX = Math.floor((num % 100) / 10);
    var iI = Math.floor(num % 10);
    return M[iM].concat(C[iC], X[iX], I[iI]);
};
