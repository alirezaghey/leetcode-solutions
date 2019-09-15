/**
 * A Queue Abstract Datastructure implemented
 * as a linked list.
 *
 * All operations are in O(1) time complexity.
 *
 */

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

class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}
