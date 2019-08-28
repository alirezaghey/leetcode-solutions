// https://leetcode.com/problems/add-two-numbers/
// Related Topics: Linked List, Math
// Difficulty: Easy

/*
Initial thoughts:
Creating a new linked list, we need to loop over the given
linked lists, adding their values and moving any remaining
carry to the next digit.
Keep in mind that some carry may remain after both the linked list
are completed. We need to add the remaining carry to the result if need be.

Time complexity: O(Max(n,m)) where n === l1.length and m === l2.length
Space complexity: O(Max(n,m)) where n === l1.length and m === l2.length

*/

var addTwoNumbers = function(l1, l2) {
  let tempRes = l1 ? l1.val : 0;
  tempRes += l2 ? l2.val : 0;
  let carry = (tempRes / 10) | 0;
  tempRes = tempRes % 10;
  const head = new ListNode(tempRes);
  let curr = head;
  l1 = l1.next;
  l2 = l2.next;

  while (l1 !== null || l2 !== null) {
    tempRes = l1 ? l1.val : 0;
    tempRes += l2 ? l2.val : 0;
    tempRes += carry;
    carry = (tempRes / 10) | 0;
    tempRes = tempRes % 10;

    curr.next = new ListNode(tempRes);
    curr = curr.next;
    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }
  if (carry) curr.next = new ListNode(carry);
  return head;
};

/*
Optimization:
Instead of calculating the first digit in the linked lists
before we enter the while loop, we can create a dummy node
at the beginning of our result linked list and return its
next node when the loop is completed.

This approach won't change time or space complexity but
it renders our code cleaner and prevents repetition.

Time complexity: O(Max(n,m)) where n === l1.length and m === l2.length
Space complexity: O(Max(n,m)) where n === l1.length and m === l2.length

*/

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let tempRes,
    carry = 0;
  const head = new ListNode(0);
  let curr = head;

  while (l1 !== null || l2 !== null) {
    tempRes = l1 ? l1.val : 0;
    tempRes += l2 ? l2.val : 0;
    tempRes += carry;
    carry = (tempRes / 10) | 0;
    tempRes = tempRes % 10;

    curr.next = new ListNode(tempRes);
    curr = curr.next;
    if (l1) l1 = l1.next;
    if (l2) l2 = l2.next;
  }
  if (carry) curr.next = new ListNode(carry);
  return head.next;
};
