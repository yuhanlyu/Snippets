/* Given a digit string, return all possible letter combinations that the 
 * number could represent.
 * Time Complexity: O(3^l)
 * Space Complexity: O(3^l), l is the length of the input
 */

/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
    if (digits.length === 0)
        return [];
    var map = ["0", "1", "abc", "def", "ghi", "jkl",
               "mno", "pqrs", "tuv", "wxyz"];
    var result = [[]];
    for (var digit of digits.split("")) {
        var temp = [];
        for (var r of result) {
            for (var d of map[parseInt(digit)].split(""))
                temp.push(r.concat([d]));
        }
        result = temp;
    }
    temp = [];
    for (var item of result)
        temp.push(item.join(""));
    return temp;
};
