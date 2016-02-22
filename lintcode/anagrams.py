class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        d = {}
        for str in strs:
            d.setdefault(''.join(sorted(str)), []).append(str)
        return [item for list in d.viewvalues() for item in list if len(list) > 1]
