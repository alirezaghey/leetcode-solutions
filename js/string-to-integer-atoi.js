//https://leetcode.com/problems/string-to-integer-atoi/
// Related Topics: Math, String
// Difficulty: Medium

/*
Initial thoughts:
Remove the first possible space character.
Handle a possible minus sign.
Handle each digit.
Check all the while that it doesn't goes outside of -2^31 or 2^31-1

Time complexity: O(n)
Space complexity: O(1)
*/

/**
 * @param {string} str
 * @return {number}
 */
const myAtoi = str => {
  const MIN = 2 ** 31 * -1;
  const MAX = MIN * -1 - 1;
  let result = 0;
  let isNegative = false;

  let i = 0;
  // move forward while white space
  while (str.charCodeAt(i) === 32) i++;

  // handle minus sign or plus sign
  if (str.charCodeAt(i) === 45 || str.charCodeAt(i) === 43) {
    if (str.charCodeAt(i) === 45) isNegative = true;
    i++;
  }

  for (; i < str.length; i++) {
    if (str.charCodeAt(i) < 48 || str.charCodeAt(i) > 57) {
      if (isNegative) return result * -1;
      else return result;
    }
    // handling the first digit
    if (result === 0) result += str.charCodeAt(i) - 48;
    else result = result * 10 + str.charCodeAt(i) - 48;

    if (isNegative && result * -1 <= MIN) return MIN;
    else if (!isNegative && result >= MAX) return MAX;
  }
  if (isNegative) return result * -1;
  else return result;
};

/*
Using regular expression10


Time complexity: O(1)
Space complexity: O(1)
*/

/**
 * @param {string} str
 * @return {number}
 */
const myAtoi = str => {
  str = str.trim();
  const MIN = 2 ** 31 * -1;
  const MAX = MIN * -1 - 1;
  let result = /^([+-]{0,1})\d+/.exec(str);
  if (!result) return 0;
  result = parseInt(result[0]);
  if (result > MAX) return MAX;
  if (result < MIN) return MIN;

  return result;
};
