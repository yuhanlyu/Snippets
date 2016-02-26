class Solution:
    """
    @param k: The number k.
    @return: The kth prime number as description.
    """
    def kthPrimeNumber(self, k):
        numbers, indices, factors = [1], [0, 0, 0], [3, 5, 7]
        for i in xrange(k):
            next = min([numbers[indices[j]] * factors[j] for j in xrange(3)])
            numbers.append(next)
            indices[:] = [indices[j] +
                          (1 if numbers[indices[j]] * factors[j] == next else 0)
                          for j in xrange(3)]
        return numbers[-1]
