/* You are a professional robber planning to rob houses along a street. Each 
 * house has a certain amount of money stashed, the only constraint stopping you
 * from robbing each of them is that adjacent houses have security system 
 * connected and it will automatically contact the police if two adjacent houses
 * were broken into on the same night.
 * Given a list of non-negative integers representing the amount of money of 
 * each house, determine the maximum amount of money you can rob tonight 
 * without alerting the police.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var steal = 0, not_steal = 0;
    for (var num of nums) {
        var temp = steal;
        steal = not_steal + num;
        not_steal = Math.max(temp, not_steal);
    }
    return Math.max(steal, not_steal);
};
