/* Say you have an array for which the ith element is the price of a given stock
 * on day i.
 * Design an algorithm to find the maximum profit. You may complete at most two 
 * transactions.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    var buy1 = -Math.pow(2, 31), buy2 = -Math.pow(2, 31)
    for (var sell1 = 0, sell2 = 0, i = 0; i < prices.length; ++i) {
        sell2 = Math.max(sell2, buy2 + prices[i])
        buy2 = Math.max(buy2, sell1 - prices[i])
        sell1 = Math.max(sell1, buy1 + prices[i])
        buy1 = Math.max(buy1, -prices[i])
    }
    return sell2
};
