/* The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */

/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    for (var i = 0, result = ['1']; i < n - 1; ++i, result = tmp) {
        for (var index = 0, count=1, tmp = []; index < result.length; ++index) {
            if (index == result.length - 1 || result[index+1] != result[index]){
                tmp = tmp.concat(count.toString().split())
                tmp.push(result[index])
                count = 1
            } else
                ++count
        }
    }
    return result.join("")
};
