/* There are N gas stations along a circular route, where the amount of gas at 
 * station i is gas[i].
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to 
 * travel from station i to its next station (i+1). You begin the journey with 
 * an empty tank at one of the gas stations.
 * Return the starting gas station's index if you can travel around the circuit 
 * once, otherwise return -1.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */

/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    for (var ac = 0, start = 0, m = 0, i = 0; i < gas.length; ++i) {
        var net_cost = gas[i] - cost[i];
        ac += net_cost;
        if (ac < m) {
            start = i + 1;
            m = ac;
        }
    }
    return ac >= 0 ? start : -1;
};
