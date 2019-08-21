// Related Topics: Linked List
// Difficulty: Easy

/*
Initial thoughts:
Creating a new list, we loop over the input lists,
compare and add them to the new list

Time complexity: O(n+m) where n === l1.length and m === l2.length
Space complexity: O(n+m) where n === l1.length and m === l2.length

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
const mergeTwoLists = (l1, l2) => {
  if (!l1 && !l2) return null;
  let head = (curr = {});

  while (l1 || l2) {
    if (!l2 || (l1 && l1.val < l2.val)) {
      curr.next = new ListNode(l1.val);
      l1 = l1.next;
      curr = curr.next;
    } else {
      curr.next = new ListNode(l2.val);
      l2 = l2.next;
      curr = curr.next;
    }
  }
  return head.next;
};

/*
Optimization:
Splicing together the input linked lists to create the results
we can render the time complexity constant.
Caveat: The input Linked Lists will be destroyed.

Time complexity: O(n+m) where n === l1.length and m === l2.length
Space complexity: O(1)
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
const mergeTwoLists = (l1, l2) => {
  if (!l1 && !l2) return null;
  let head = (curr = {});
  while (l1 || l2) {
    if (!l2 || (l1 && l1.val < l2.val)) {
      curr.next = l1;
      l1 = l1.next;
      curr = curr.next;
    } else {
      curr.next = l2;
      l2 = l2.next;
      curr = curr.next;
    }
  }
  return head.next;
};
