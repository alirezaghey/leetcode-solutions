// https://leetcode.com/problems/valid-anagram/
// Related Topics: Hash Table, Sort
// Difficulty: Easy

/*
Initial thoughts:
For a word to be an anagram of another word, it must have the exact
same characters with the same quanitity as the other word, just in a
different ordering.
Using a hash map, we can create a frequency table from the first word
and remove them from the frequency table while we go through the second
word.
If at the end the frequency table is empty, we have an anagram

Time complexity: O(n) where n == len(s)
Space complexity: O(1) because the freq tables won't have more than 26 chars
(even if we were dealing with the whole unicode spectrum, it would be of constant
complexity)
*/

/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
const isAnagram = (s, t) => {
    const m = new Map();
    for (const c of s) {
        if (m.has(c)) m.set(c, m.get(c) + 1);
        else m.set(c, 1);
    }
    for (const c of t) {
        if (m.has(c)) {
            if (m.get(c) == 1) m.delete(c);
            else m.set(c, m.get(c) - 1);
        } else return false;
    }
    return m.size === 0;
};
