class Node:
    def __init__(self, v):
        self.v = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None

    def add(self, v):
        def add_helper(node, v):
            if not node:
                return Node(v)
            node.next = add_helper(node.next, v)
            return node
        self.root = add_helper(self.root, v)

    def contains(self, v):
        node = self.root
        while node:
            if node.v == v:
                return True
        return False

    def remove(self, v):
        def remove_helper(node, v):
            if not node:
                return None
            if node.v == v:
                return node.next
            node.next = remove_helper(node.next, v)
            return node
        self.root = remove_helper(self.root, v)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 100000
        self.size = 0
        self.ratio = 0.8
        self.data = [None] * self.capacity

    def add(self, key: int) -> None:
        hashed_key = hash(key)
        bucket = hashed_key % self.capacity
        linked_list = self.data[bucket]
        if not linked_list:
            linked_list = self.data[bucket] = LinkedList()

        if linked_list.contains(key):
            return

        linked_list.add(key)
        self.size += 1
        if self.size / self.capacity > self.ratio:
            self.resize()

    def remove(self, key: int) -> None:
        hashed_key = hash(key)
        bucket = hashed_key % self.capacity
        linked_list = self.data[bucket]
        if not linked_list:
            return
        if not linked_list.contains(key):
            return

        linked_list.remove(key)
        self.size -= 1

        if self.size / self.capacity < self.ratio/2:
            self.resize()

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashed_key = hash(key)
        bucket = hashed_key % self.capacity
        linked_list = self.data[bucket]
        if not linked_list:
            return False
        return linked_list.contains(key)

    def resize(self):
        pass


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
