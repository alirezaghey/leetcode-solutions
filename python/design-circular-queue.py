class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._data = [None for i in range(k)]
        self._size = k
        self._back = 0
        self._front = 0
        self._empty = True

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self._back == self._front and self._empty == False:  # The circular queue is full
            return False
        # print("hello")
        self._data[self._back] = value
        self._back = (self._back+1) % self._size
        self._empty = False
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self._empty == True:
            return False
        self._data[self._front] = None
        self._front = (self._front+1) % self._size
        if self._front == self._back:
            self._empty = True
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self._empty:
            return -1
        return self._data[self._front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self._empty:
            return -1
        temp = self._back - 1 if self._back != 0 else self._size-1
        return self._data[temp]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._empty

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._front == self._back and self._empty == False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
