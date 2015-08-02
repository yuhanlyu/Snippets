# There are N children standing in a line. Each child is assigned a rating 
# value.
# You are giving candies to these children subjected to the following 
# requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        result, prev, peak, peakn = 1, 1, 0, 1
        for i in xrange(1, len(ratings)):
            if ratings[i] < ratings[i - 1]:
                if peakn == i - peak:
                    result, peakn = result + 1, peakn + 1
                result, prev = result + i - peak, 1
            elif ratings[i] > ratings[i - 1]:
                prev += 1
                result, peak, peakn = result + prev, i, prev
            else:
                result, prev, peak, peakn = result + 1, 1, i, 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.candy([1,2,3,6,5,4,3,2,1])
