/* Implement the following operations of a queue using stacks.
 * Time Complexity: amortized O(1) for each operation
 * Space Complexity: O(n)
 */

/**
 * @constructor
 */
var Queue = function() {
    this.front = [];
    this.end = [];
};

/**
 * @param {number} x
 * @returns {void}
 */
Queue.prototype.push = function(x) {
    this.end.push(x);
};

/**
 * @returns {void}
 */
Queue.prototype.pop = function() {
    this.peek();
    return this.front.pop();
};

/**
 * @returns {number}
 */
Queue.prototype.peek = function() {
    if (this.front.length === 0) {
        while (this.end.length > 0)
            this.front.push(this.end.pop());
    }
    return this.front[this.front.length - 1];
};

/**
 * @returns {boolean}
 */
Queue.prototype.empty = function() {
    return this.front.length === 0 && this.end.length === 0;
};
