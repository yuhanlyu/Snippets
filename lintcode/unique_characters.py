class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        return len(set([c for c in str])) == len(str)
