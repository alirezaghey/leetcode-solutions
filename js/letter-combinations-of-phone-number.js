// https://leetcode.com/problems/letter-combinations-of-a-phone-number/solution/
//  Related Topics: String, Backtracking
//  Difficulty: Medium

// Time complexity: O(3^n * 4^m) where n === number of digits that have 3 corresponding chars and
// m === numer of digits that have 4 corresponding chars
// Space complexit: O(3^n * 4^m)

/**
 * @param {string} digits
 * @return {string[]}
 */
const letterCombinations = digits => {
  if (digits.length === 0) return [];
  lookup = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
  };
  results = [];
  permute(lookup, '', digits, results);
  return results;
};

const permute = (lookup, combination, remaining, results) => {
  if (remaining.length === 0) {
    results.push(combination);
    return;
  }
  for (let i = 0; i < lookup[remaining[0]].length; i++) {
    permute(
      lookup,
      combination + lookup[remaining[0]][i],
      remaining.slice(1),
      results
    );
  }
};
