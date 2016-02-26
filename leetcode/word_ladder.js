/* Given two words (beginWord and endWord), and a dictionary, find the length 
 * of shortest transformation sequence from beginWord to endWord, such that:
 * Only one letter can be changed at a time
 * Each intermediate word must exist in the dictionary
 * Time Complexity: O(n 26^l), l is the length of each word
 * Space Complexity: O(n)
 */

/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {Set} wordList
 *   Note: wordList is a Set object, see:
 *   https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    queue = [[beginWord, 1]];
    wordList.add(endWord);
    for (var new_queue = []; queue.length; queue = new_queue) {
        for (new_queue = []; queue.length;) {
            var temp = queue.pop();
            var str = temp[0];
            var length = temp[1];
            for (var i = 0; i < str.length; ++i) {
                var original = str.charAt(i);
                var prefix = str.substring(0, i);
                var suffix = str.substring(i + 1);
                for (var c of "abcdefghijklmnopqrstuvwxyz") {
                    if (c !== original) {
                        var new_str = prefix.concat(c, suffix);
                        if (wordList.has(new_str)) {
                            if (new_str === endWord)
                                return length + 1;
                            new_queue.push([new_str, length + 1]);
                            wordList.delete(new_str);
                        }
                    }
                }
            }
        }
    }
    return 0;
};
