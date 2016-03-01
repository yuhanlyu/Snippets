class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        period = n.index(".")
        integral, n = bin(int(n[:period]))[2:], float(n[period:])
        if n == 0: return integral
        fractional = []
        for i in xrange(32):
            b = pow(2, -(i + 1))
            fractional.append("1" if n >= b else "0")
            n %= b
            if n == 0:
                return integral + "." + "".join(fractional)
        return "ERROR"
