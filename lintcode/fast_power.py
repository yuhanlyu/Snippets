class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        result = 1
        while n > 0:
            if n & 1:
                result = (result * a) % b
            n /= 2
            a = (a * a) % b
        return result % b
