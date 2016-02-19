/* Given an array of integers, every element appears three times except for one.
 * Find that single one.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    var one = 0, two = 0;
    for (var num of nums) {
        one = (one ^ num) & ~two;
        two = (two ^ num) & ~one;
    }
    return one
};
