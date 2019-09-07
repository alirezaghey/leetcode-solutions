// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Related Topics: Hash Table, Two Pointers, String, Sliding Window
// Difficulty: Medium

/*
Initial thoughts:
Using a sliding window we start at the beginning of the array
and continuously move the right side of the window to the right,
all the while adding each element to a Set.
If the character is recurring, we start another sliding window
with the left side moved forward by one elemenet.
The size of the biggest possible sliding window is the
longest substring without repeating chars.

Time complexity: O(n^2) where n is the number of elements
Space complexity: O(min(n,m)) where n is the number of elements and
m is the number of characters in the alphabet

*/

/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;
  let maxLength = 0;

  for (let i = 0; i < s.length; i++) {
    const set = new Set([s[i]]);
    for (let j = i + 1; j < s.length; j++) {
      if (set.has(s[j])) break;
      set.add(s[j]);
    }
    maxLength = Math.max(maxLength, set.size);
  }
  return maxLength;
};

/*
Optimization:
Since we are looking for the longest substring
we can stop looping if the left side of the sliding window
has reached a point where the rest of the potential substrings
won't be longer than the already found maxLength.

This won't change the time complexity since in a worst case scenario
we won't find anything, or the longest possible substring until we reach
the end of the loop.

Time complexity: O(n^2) where n is the number of elements
Space complexity: O(min(n, m)) where n is the number of elements and
m is the number of characters in the alphabet
*/

/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;
  let maxLength = 0;

  for (let i = 0; i < s.length - maxLength; i++) {
    const set = new Set([s[i]]);
    for (let j = i + 1; j < s.length; j++) {
      if (set.has(s[j])) break;
      set.add(s[j]);
    }
    maxLength = Math.max(maxLength, set.size);
  }
  return maxLength;
};

/*
Optimization:
In our previous approaches we used to start over checking
every character after the left side of our sliding window
moved forward.
The here is to keep our Set and just remove the left most element
from it when the left side of the sliding window moves forward.
This approach enables us to reuse the already added items to the Set,
decreasing our time complexity by one degree.

Time complexity: O(n) where n is the number of elements in the array
Space complexity: O(min(n,m)) where n is the number of elements in the array
and m is the number of characters in the alphabet
*/

/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;

  let left = (right = 0);
  let maxLength = 0;
  let set = new Set();
  while (left < s.length && right < s.length) {
    if (!set.has(s[right])) {
      set.add(s[right]);
      maxLength = Math.max(maxLength, set.size);
      right++;
    } else {
      set.delete(s[left]);
      left++;
    }
  }
  return maxLength;
};

/*
Optimization:
Building on the previous approach, we can exit the loop
if the left side of the sliding window becomes greater
than s.length - maxLength because there can't be a potentially
bigger substring.

Time complexity: O(n) where n is the number of elements in the array
Space complexity: O(min(n,m)) where n is the number of elements in the array
and m is the number of characters in the alphabet
*/

/**
 * @param {string} s
 * @return {number}
 */

const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;

  let left = (right = 0);
  let maxLength = 0;
  const set = new Set();
  while (left < s.length - maxLength && right < s.length) {
    if (!set.has(s[right])) {
      set.add(s[right]);
      maxLength = Math.max(maxLength, set.size);
      right++;
    } else {
      set.delete(s[left]);
      left++;
    }
  }
  return maxLength;
};

/*
Optimization:
Instead of using a Set we could use a Map and keeping track of
each characters index.
Now, when we encounter a duplicated character, instead of moving
the left side of the window by one, we could jump to the position
where the repeating character is + one.
This way, we are going to decrease the time complexity from O(2n) to O(n) which
isn't actually an optimization in terms of Big O, but it's still a small gain.

Time complexity: O(n) where n is the number of elements in the array
Space complexity: O(min(n,m)) where n is the number of elements in the array
and m is the number of characters in the alphabet
*/

/**
 * @param {string} s
 * @returns {number}
 */

const lengthOfLongestSubstring = s => {
  if (s.length === 0) return 0;

  let maxLength = 0;
  const map = new Map();

  for (let j = 0, i = 0; j < s.length; j++) {
    if (map.has(s[j])) {
      i = Math.max(map.get(s[j]), i);
    }
    maxLength = Math.max(maxLength, j - i + 1);
    map.set(s[j], j + 1);
  }
  return maxLength;
};
