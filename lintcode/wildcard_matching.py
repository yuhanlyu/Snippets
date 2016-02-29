class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        i, j, match, star = 0, 0, 0, -1
        while i < len(s):
            if j < len(p) and (p[j] == '?' or s[i] == p[j]):
                i, j = i + 1, j + 1
            elif j < len(p) and p[j] == '*':
                star, match, j = j + 1, i + 1, j + 1
            elif star >= 0:
                i, j, match = match, star, match + 1
            else: return False
        while j < len(p) and p[j] == '*':
            j += 1
        return j == len(p)
