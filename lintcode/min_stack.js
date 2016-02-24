/* Design a stack that supports push, pop, top, and retrieving the minimum 
 * element in constant time.
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * getMin() -- Retrieve the minimum element in the stack.
 */

/**
 * @constructor
 */
var MinStack = function() {
    this.stack = [];
    this.minValues = [];
};

/**
 * @param {number} x
 * @returns {void}
 */
MinStack.prototype.push = function(x) {
    this.stack.push(x);
    if (this.minValues.length === 0 || x <= this.getMin())
        this.minValues.push(x);
};

/**
 * @returns {void}
 */
MinStack.prototype.pop = function() {
    if (this.top() === this.getMin())
        this.minValues.pop();
    return this.stack.pop();
};

/**
 * @returns {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1];
};

/**
 * @returns {number}
 */
MinStack.prototype.getMin = function() {
    return this.minValues[this.minValues.length - 1];
};
