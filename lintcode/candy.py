class Solution:
    # @param {int[]} ratings Children's ratings
    # @return {int} the minimum candies you must give
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
