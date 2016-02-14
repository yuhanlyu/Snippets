/* Given a triangle, find the minimum path sum from top to bottom. 
 * Each step you may move to adjacent numbers on the row below.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    for (var i = triangle.length - 2; i >= 0; --i)
        for (var j = 0; j < triangle[i].length; ++j)
            triangle[i][j] += Math.min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]
};
