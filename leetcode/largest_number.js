/* Given a list of non negative integers, arrange them such that 
 * they form the largest number.
 * Time Complexity: O(n lg n)
 * Space Complexity: O(n)
 */

/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    var list = [];
    for (var num of nums)
        list.push(num.toString());
    list.sort(function(a, b) { return b.concat(a).localeCompare(a.concat(b));});
    var result = list.join("").replace(/^0+/, '');
    return result.length > 0 ? result : '0';
};
