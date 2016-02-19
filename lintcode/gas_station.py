class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        ac = start = m = 0
        for i, net_cost in enumerate((g - c for (g, c) in zip(gas, cost))):
            ac += net_cost
            if ac < m: start, m = i + 1, ac
        return start if ac >= 0 else -1
