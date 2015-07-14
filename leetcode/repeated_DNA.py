# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to 
# identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) that 
# occur more than once in a DNA molecule.
# Time Complexity: O(n) in average
# Space Complexity: O(n)

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        appear, code, result = dict(), 0, []
        for i in xrange(len(s)):
            code = ((8 * code) & 0x3FFFFFFF) | (ord(s[i]) & 7)
            if i < 9: continue
            if appear.get(code, 0) == 1:
                result.append(s[i - 9:i + 1])
            appear.setdefault(code, 0)
            appear[code] += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
