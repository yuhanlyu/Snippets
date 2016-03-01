/* You are given an array x of n positive numbers. You start at point (0,0) 
 * and moves x[0] metres to the north, then x[1] metres to the west, x[2] 
 * metres to the south, x[3] metres to the east and so on. In other words, 
 * after each move your direction changes counter-clockwise.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */


/**
 * @param {number[]} x
 * @return {boolean} 
 */
 
var isSelfCrossing = function(x) {
    var arr = new Array(5);
    arr.fill(0);
    for (var a of x) {
        if (arr[2] >= arr[0] && arr[0] > 0 
         && (a >= arr[1] || (a >= arr[1] - arr[3] && arr[1] - arr[3] >= 0 
                            && arr[4] >= arr[2] - arr[0])))
            return true;
        arr.pop();
        arr.unshift(a);
    }
    return false;
};
