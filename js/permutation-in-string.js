// https://leetcode.com/problems/permutation-in-string/
// Related Topics: Two Pointers, Sliding Window, Hash Table
// Difficulty: Medium

/*
Initial thoughts:
Creating a frequency table for the characters in s1 we are going to
have a changing frequency table for s2 that encompasses chracters equal
to the length of s1. Moving forward with the freq table on s2, we are going
to compare the two freq tables at each step. If they are identical, we have a
permutation of s1 in s2.
Since we are dealing with a predefined set of characters (in this case English
small letters) the comparision of the freq tables takes constant time (26 at most)
Creating the freq tables also won't take more than linear time equal to the length
of s2.

Time complexity: O(n) where n == len(s2)
Space complexity: O(1) because the freq tables won't have more than 26 chars
*/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
const checkInclusion = (s1, s2) => {
    const dic1 = createFreqTable(s1);
    const dic2 = createFreqTable(s2.slice(0, s1.length));

    if (compareDics(dic1, dic2)) return true;
    for (let i = s1.length; i < s2.length; i++) {
        dic2.set(s2[i - s1.length], dic2.get(s2[i - s1.length]) - 1);
        if (dic2.has(s2[i])) dic2.set(s2[i], dic2.get(s2[i]) + 1);
        else dic2.set(s2[i], 1);
        if (dic2.get(s2[i - s1.length]) === 0) dic2.delete(s2[i - s1.length]);
        if (compareDics(dic1, dic2)) return true;
    }
    return false;

    function compareDics(dic1, dic2) {
        if (dic1.size !== dic2.size) return false;
        for (const k of dic1.keys()) {
            if (dic2.has(k) && dic1.get(k) === dic2.get(k)) continue;
            return false;
        }
        return true;
    }
    function createFreqTable(s) {
        m = new Map();
        for (let c of s) {
            if (m.has(c)) m.set(c, m.get(c) + 1);
            else m.set(c, 1);
        }
        return m;
    }
};
