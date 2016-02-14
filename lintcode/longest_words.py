class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        max = 0
        for i in xrange(1, len(dictionary)):
            if len(dictionary[i]) > max:
                max = len(dictionary[i])
        return [x for x in dictionary if len(x) == max]
