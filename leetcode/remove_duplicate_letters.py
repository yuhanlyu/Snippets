# Given a string which contains only lowercase letters, remove duplicate 
# letters so that every letter appear once and only once. You must make sure 
# your result is the smallest in lexicographical order among all possible 
# results.
# Time Complexity: O(n)
# Space Complexity: O(n)

import collections

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = collections.defaultdict(int)
        for c in s:
            cnts[c] += 1
        stack, instack = [" "], set()
        for i, c in enumerate(s):
            cnts[c] -= 1
            if c in instack:
                continue
            while c < stack[-1] and cnts[stack[-1]]:
                instack.remove(stack.pop())
            stack.append(c)
            instack.add(c)
        return ''.join(stack[1:])
                

if __name__ == "__main__":
    solution = Solution()
    print solution.removeDuplicateLetters("bcabc")
    print solution.removeDuplicateLetters("cbacdcbc")
