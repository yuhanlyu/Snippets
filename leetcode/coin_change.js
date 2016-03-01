/* You are given coins of different denominations and a total amount of money 
 * amount. Write a function to compute the fewest number of coins that you 
 * need to make up that amount. If that amount of money cannot be made up by 
 * any combination of the coins, return -1.
 * Time Complexity: O(n amount)
 * Space Complexity: O(amount)
 */

/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    var DP = new Array(amount + 1);
    DP.fill(amount + 1);
    DP[0] = 0;
    for (var coin of coins) {
        DP[coin] = 1;
        for (var i = coin + 1; i <= amount; ++i)
            if (DP[i - coin] + 1 < DP[i])
                DP[i] = DP[i - coin] + 1;
    }
    return DP[amount] <= amount ? DP[amount] : -1;
};
