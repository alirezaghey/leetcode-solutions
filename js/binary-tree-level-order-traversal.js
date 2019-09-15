// https://leetcode.com/problems/binary-tree-level-order-traversal/
// Related Topics: Tree, BFS
// Difficulty: Easy

/*
Initial thoughts:
Using a BFS approach, we are going to queue the nodes for the next level
in a temporary queue and visit each node in the current queue while adding
their children to the temp queue.
When the current queue is empty, we are going to make the temp queue,
the current queue and start the process again untill there is no node left.
[JS Note]: Since JavaScript does not have a default Queue data structure and
using JS arrays as a queue will has an O(n) time complexity when shifting the head
we will create our own Queue abstract datatype based on a singly linked list.

Time complexity: O(n) where n is the number of nodes in the tree
Space complexity: O(n) where n is the number of nodes in the tree;
That is because we need to temporarily queue the nodes in a particular level
and since the last level of a binary tree holds approximately n/2 nodes, the
space complelxity is O(n) 

*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
const levelOrder = root => {
  let currQueue = new Queue();
  currQueue.enqueue(root);
  let tempQueue = new Queue();

  const result = [];
  let tempRes = [];

  while (currQueue.length > 0) {
    const node = currQueue.dequeue();
    if (node !== null) {
      tempRes.push(node.val);
      tempQueue.enqueue(node.left);
      tempQueue.enqueue(node.right);
    }
    if (currQueue.length === 0) {
      if (tempRes.length > 0) result.push(tempRes);
      tempRes = [];
      currQueue = tempQueue;
      tempQueue = new Queue();
    }
  }
  return result;
};

/*
A JavaScript implementation misusing JS arrays as Queue
 */

/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
const levelOrder = root => {
  let currQueue = [root];
  let tempQueue = [];
  let result = [];
  let tempRes = [];

  while (currQueue.length > 0) {
    const node = currQueue.shift();
    if (node !== null) {
      tempRes.push(node.val);
      tempQueue.push(node.left);
      tempQueue.push(node.right);
    }
    if (currQueue.length === 0) {
      if (tempRes.length !== 0) result.push(tempRes);
      currQueue = tempQueue;
      tempQueue = [];
      tempRes = [];
    }
  }
  return result;
};

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  enqueue(data) {
    const node = new Node(data);
    if (this.head === null) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.length++;
  }

  dequeue() {
    if (this.head === null) return null;
    else {
      if (this.head === this.tail) {
        const node = this.head;
        this.head = this.tail = null;
        this.length--;
        return node.data;
      } else {
        const node = this.head;
        this.head = this.head.next;
        this.length--;
        return node.data;
      }
    }
  }

  peek() {
    if (this.head !== null) return this.head.data;
    else return null;
  }
}
