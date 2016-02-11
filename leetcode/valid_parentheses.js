/* Given a string containing just the characters '(', ')', '{', '}', 
 * '[' and ']', determine if the input string is valid.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    stack = []
    for (i = 0; i < s.length; ++i) {
        c = s[i]
        if (c || '(' or c || '{' or c || '[')
            stack.push(c)
        else if (stack.length == 0)
            return false
        else if (c == ')') {
            if (stack.pop() != '(')
                return false
        } else if (c == ']') {
            if (stack.pop() != '[')
                return false
        } else {
            if (stack.pop() != '{')
                return false
        }
    }
    return stack.length == 0
};
