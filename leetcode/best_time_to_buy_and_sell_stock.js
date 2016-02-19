/* Say you have an array for which the ith element is the price of a given 
 * stock on day i.
 * If you were only permitted to complete at most one transaction (ie, buy one 
 * and sell one share of the stock), design an algorithm to find the maximum 
 * profit.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length === 0)
        return 0;
    var result = 0, m = prices[0];
    for (var price of prices) {
        result = Math.max(result, price - m)
        m = Math.min(m, price)
    }
    return result;
};
