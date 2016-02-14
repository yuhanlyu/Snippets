class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        a, result = a ^ b, 0
        a = a if a >= 0 else a + 2 ** 32
        while a != 0:
            result += 1
            a &= a - 1
        return result
