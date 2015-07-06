# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, 
# otherwise return 0.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        index1, index2 = 0, 0
        while index1 < len(version1) or index2 < len(version2):
            v1, v2 = 0, 0
            while index1 < len(version1) and version1[index1] != '.':
                v1 = v1 * 10 + int(version1[index1])
                index1 += 1
            while index2 < len(version2) and version2[index2] != '.':
                v2 = v2 * 10 + int(version2[index2])
                index2 += 1
            if v1 > v2:
                return 1
            if v2 > v1:
                return -1
            index1 += 1
            index2 += 1
        return 0

if __name__ == "__main__":
    solution = Solution()
    print solution.compareVersion("0.1", "1.1")
    print solution.compareVersion("1.1", "1.1")
    print solution.compareVersion("1.1.1", "1.1")
    print solution.compareVersion("1", "1.0.0")
