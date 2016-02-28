class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndexII(self, A):
        map, m, fac, result = {}, 1, 1, 1
        for i in xrange(len(A) - 1, -1, -1):
            map[A[i]] = map.get(A[i], 0) + 1
            m *= map[A[i]]
            c = sum([1 for j in xrange(i + 1, len(A)) if A[i] > A[j]])
            result += c * fac / m
            fac *= len(A) - i
        return result 
