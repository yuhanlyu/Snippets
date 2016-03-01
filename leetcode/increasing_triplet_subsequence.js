/* Given an unsorted array return whether an increasing subsequence of length 
 * 3 exists or not in the array.
 */


/**
 * @param {number[]} nums
 * @return {boolean}
 */
var increasingTriplet = function(nums) {
    var arr = [Infinity, Infinity];
    for (var num of nums) {
        if (num <= arr[0])
            arr[0] = num;
        else if (num <= arr[1])
            arr[1] = num;
        else
            return true;
    }
    return false;
};
