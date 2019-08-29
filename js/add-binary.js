// https://leetcode.com/problems/add-binary/
// Related Topics: Math, String
// Difficulty: Easy

/*
Initial thoughts:
Looping over both arrays from the end backwards we are going to
add the corresponding digits of both of the arrays (if there is none for one of them then zero),
all the while taking care of a possible remainder and carrying it to the next left digit.
At the end we need to take care of a potential remainder and add it to the array.

For performance purposes, we are going to create the result in a reversed array and reverse it
at the end.
That is because pushing to an array is way more efficient than unshifting. A single reversal at
the end of the algorithm is just O(n) and doable.
Another workaround would be to use a doubly linked list and convert it to an array at the end
of the algorithm which would also be no more than an additional O(n).

Time complexity: O(Max(n,m)) where n === a.length and m === b.length
Space complexity: O(Max(n,m)) where n === a.length and m === b.length

*/

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
const addBinary = (a, b) => {
  const result = [];
  let carry = 0;

  for (let i = a.length - 1, j = b.length - 1; i >= 0 || j >= 0; i--, j--) {
    let res = (Number(a[i]) | 0) + (Number(b[j]) | 0) + carry;
    carry = (res / 2) | 0;
    res = res % 2;
    result.push(res);
  }
  if (carry) result.push(carry);
  return result.reverse().join('');
};
