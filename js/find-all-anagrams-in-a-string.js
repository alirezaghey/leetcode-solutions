// https://leetcode.com/problems/find-all-anagrams-in-a-string/
// Related Topics: Two Pointers, Sliding Window, Hash Table
// Difficulty: Medium

/*
Initial thoughts:
Creating a frequency table for the characters in p we are going to
have a changing frequency table for s that encompasses chracters equal
to the length of p. Moving forward with the freq table on s, we are going
to compare the two freq tables at each step. If they are identical, we have an
anagram of p in s and we are going to save the anagram's index in s in a result array.
Since we are dealing with a predefined set of characters (in this case English
small letters) the comparison of the freq tables takes constant time (26 at most)
Creating the freq tables also won't take more than linear time equal to the length
of s.

Time complexity: O(n) where n == len(s)
Space complexity: O(1) because the freq tables won't have more than 26 chars
*/
/**
 * @param {string} s
 * @param {string} p
 * @return {number[]}
 */
const findAnagrams = (s, p) => {
    const dicP = createFreqTable(p);
    const dicS = createFreqTable(s.slice(0, p.length));
    const res = [];
    if (compareDics(dicP, dicS)) res.push(0);
    for (let i = p.length; i < s.length; i++) {
        if (dicS.has(s[i])) dicS.set(s[i], dicS.get(s[i]) + 1);
        else dicS.set(s[i], 1);
        if (dicS.get(s[i - p.length]) === 1) dicS.delete(s[i - p.length]);
        else dicS.set(s[i - p.length], dicS.get(s[i - p.length]) - 1);
        if (compareDics(dicP, dicS)) res.push(i - p.length + 1);
    }
    return res;

    function compareDics(dic1, dic2) {
        if (dic1.size !== dic2.size) return false;
        for (key of dic1.keys()) {
            if (dic2.has(key) && dic1.get(key) === dic2.get(key)) continue;
            return false;
        }
        return true;
    }

    function createFreqTable(s) {
        const m = new Map();
        for (const c of s) {
            if (m.has(c)) m.set(c, m.get(c) + 1);
            else m.set(c, 1);
        }
        return m;
    }
};
