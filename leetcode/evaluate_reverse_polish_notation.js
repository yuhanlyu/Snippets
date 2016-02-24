/* Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * Valid operators are +, -, *, /. 
 * Each operand may be an integer or another expression.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function(tokens) {
    var plus = function(a, b) { return b + a; };
    var sub  = function(a, b) { return b - a; };
    var mul  = function(a, b) { return b * a; };
    var div  = function(a, b) { return a * b >= 0 ? Math.floor(b / a) : Math.ceil(b / a); };
    var oprs = [], ops = [plus, sub, mul, div];
    for (var token of tokens) {
        if (token.length === 1 && '+-*/'.indexOf(token) !== -1)
            oprs.push(ops['+-*/'.indexOf(token)].call(null, oprs.pop(), oprs.pop()));
        else
            oprs.push(parseInt(token));
    }
    return oprs[0];
};
