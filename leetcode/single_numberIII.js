/* Given an array of numbers nums, in which exactly two elements appear only 
 * once and all the other elements appear exactly twice. 
 * Find the two elements that appear only once.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var singleNumber = function(nums) {
    var xor = 0, ans = 0;
    for (var num of nums)
        xor ^= num
    for (num of nums)
        if (xor & -xor & num)
            ans ^= num
    return [xor ^ ans, ans]
};
