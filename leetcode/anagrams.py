# Given an array of strings, return all groups of strings that are anagrams.
# Time Complexity: O(nm lg m), n is the number of strings, m is the length
# Space Complexity: O(nm)

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        d = {}
        for str in strs:
            d.setdefault(''.join(sorted(str)), []).append(str)
        return [item for list in d.values() for item in list if len(list) > 1]

if __name__ == "__main__":
    solution = Solution()
    print solution.anagrams(["", ""])
