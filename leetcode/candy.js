/* There are N children standing in a line. Each child is assigned a rating 
 * value.
 * You are giving candies to these children subjected to the following 
 * requirements:
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.
 * What is the minimum candies you must give?
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    var result = 1, prev = 1, peak = 0, peakn = 1;
    for (var i = 1; i < ratings.length; ++i) {
        if (ratings[i] < ratings[i - 1]) {
            if (peakn === i - peak) {
                ++result;
                ++peakn;
            }
            result += i - peak;
            prev = 1;
        } else if (ratings[i] > ratings[i - 1]) {
            result += ++prev;
            peak = i;
            peakn = prev;
        } else {
            ++result;
            peak = i;
            peakn = prev = 1;
        }
    }
    return result;
};
