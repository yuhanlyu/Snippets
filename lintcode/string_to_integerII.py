class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        INT_MAX, INT_MIN, THRESHOLD = 2147483647, -2147483648, 214748364
        start, sign, result, index = False, 1, 0, 0
        while index < len(str) and str[index] == ' ':
            index += 1
        if index < len(str) and (str[index] == '+' or str[index] == '-'):
            sign = 1 if str[index] == '+' else -1
            index += 1
        while index < len(str) and str[index].isdigit():
            c = str[index]
            if result > THRESHOLD or (result == THRESHOLD and int(c) > 7):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + int(c)
            index += 1
        return result * sign
