/* Given a string array words, find the maximum value of length(word[i]) * 
 * length(word[j]) where the two words do not share common letters. 
 * You may assume that each word will contain only lower case letters. 
 * If no such two words exist, return 0.
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */


/**
 * @param {string[]} words
 * @return {number}
 */
var maxProduct = function(words) {
    var mask = [], result = 0;
    for (var i = 0; i < words.length; ++i) {
        var m = 0;
        for (var c of words[i])
            m |= 1 << (c.charCodeAt(0) - 'a'.charCodeAt(0));
        mask.push(m);
        for (var j = 0; j < i; ++j)
            if (words[i].length * words[j].length > result 
            && ((mask[i] & mask[j]) === 0))
                result = words[i].length * words[j].length;
    }
    return result;
};
