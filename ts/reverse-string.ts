/**
 Do not return anything, modify s in-place instead.
 */
// Time complexity: O(n)
// Space complexity: O(1)
const reverseString = function (s: string[]): void {
    for (let i = 0; i < Math.floor(s.length / 2); i++) {
        [s[i], s[s.length - i - 1]] = [s[s.length - i - 1], s[i]]
    }
};