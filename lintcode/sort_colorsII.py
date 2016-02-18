class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        count = [0] * (k + 1)
        for x in colors:
            count[x] += 1
        tail = 0
        for i in xrange(1, k + 1):
            for j in xrange(count[i]):
                colors[tail] = i
                tail += 1
