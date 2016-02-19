/* Say you have an array for which the ith element is the price of a given 
 * stock on day i.
 * Design an algorithm to find the maximum profit. You may complete as many 
 * transactions as you like (ie, buy one and sell one share of the stock 
 * multiple times). However, you may not engage in multiple transactions at the 
 * same time (ie, you must sell the stock before you buy again).
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    for (var result = 0, i = 1; i < prices.length; ++i)
        result += Math.max(0, prices[i] - prices[i - 1]);
    return result;
};
