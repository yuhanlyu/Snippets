/* Given a roman numeral, convert it to an integer.
 * Input is guaranteed to be within the range from 1 to 3999.
 * Time complexity: O(n)
 * Space complexity: O(1)
 */

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    var map = new Map();
    map.set('M', 1000);
    map.set('D', 500);
    map.set('C', 100);
    map.set('L', 50);
    map.set('X', 10);
    map.set('V', 5);
    map.set('I', 1);
    var result = map.get(s.charAt(s.length - 1));
    var previous = result;
    for (var i = s.length - 2; i >= 0; --i) {
        var val = map.get(s.charAt(i));
        result += val >= previous ? val : -val;
        previous = val;
    }
    return result;
};
