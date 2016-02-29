/* Given n non-negative integers representing the histogram's bar height where 
 * the width of each bar is 1, find the area of largest rectangle in the 
 * histogram
 * Time Complexity: O(n)
 * Space Complexity: O(1) assuming input is modifiable
 */

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    heights.push(0);
    for (var result = 0, i = 0; i < heights.length; ++i) {
        for (var j = i - 1; j >= 0 && heights[j] > heights[i]; ) {
            result = Math.max(result, heights[j] * (i - j));
            heights[j--] = heights[i];
        }
    }
    return result;
};
