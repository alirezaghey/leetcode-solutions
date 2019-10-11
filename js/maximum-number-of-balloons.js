// https://leetcode.com/problems/maximum-number-of-balloons/
// Related Topics: Hash Table, String
// Difficulty: Easy

/*
Initial thoughts:
Using a hash table we are going to count the frequency of the letters
b,a,l,o, and n. Taking the floor division of the letters l and o
(because we need two of them of the word balloon) we are going to take
the minium number in the values of the frequency table.

Time complexity: O(n) where n === len(text)
Space complexity: O(1)
*/

/**
 * @param {string} text
 * @return {number}
 */
const maxNumberOfBalloons = text => {
  freqTable = 'balon'.split('').reduce((acc, el) => {
    acc[el] = 0;
    return acc;
  }, {});
  for (char of text) if (freqTable[char] !== undefined) freqTable[char]++;
  freqTable['l'] = Math.floor(freqTable['l'] / 2);
  freqTable['o'] = Math.floor(freqTable['o'] / 2);
  return Math.min(...Object.values(freqTable));
};
