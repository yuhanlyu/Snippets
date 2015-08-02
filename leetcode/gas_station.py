# There are N gas stations along a circular route, where the amount of gas at 
# station i is gas[i].
# You have a car with an unlimited gas tank and it costs cost[i] of gas to 
# travel from station i to its next station (i+1). You begin the journey with 
# an empty tank at one of the gas stations.
# Return the starting gas station's index if you can travel around the circuit 
# once, otherwise return -1.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        ac = start = m = 0
        for i, net_cost in enumerate((g - c for (g, c) in zip(gas, cost))):
            ac += net_cost
            if ac < m: start, m = i + 1, ac
        return start if ac >= 0 else -1

if __name__ == "__main__":
    solution = Solution()
    print solution.canCompleteCircuit([1, 2, 0], [1, 1, 1])
