class Solution:
    # @param {int[][]} matrix an integer matrix
    # @return {int[][]} the coordinate of the left-up and right-down number
    def submatrixSum(self, matrix):
        for i in xrange(len(matrix)):
            sum = [0] * len(matrix[i])
            for j in xrange(i, len(matrix)):
                map, cur = {0 : -1}, 0
                for k in xrange(len(matrix[j])):
                    sum[k] += matrix[j][k]
                    cur += sum[k]
                    if cur in map:
                        return [(i, map[cur] + 1), (j, k)]
                    map[cur] = k
