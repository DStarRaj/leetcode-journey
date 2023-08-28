class Queue:
    def __init__(self) -> None:
        self.__queue = []

    def enqueue(self, val: int) -> None:
        self.__queue.append(val)

    def dequeue(self) -> int:
        if not self.isEmpty():
            val = self.__queue[0]
            self.__queue = self.__queue[1:]
            return val

    def size(self) -> int:
        return len(self.__queue)

    def isEmpty(self) -> bool:
        return not bool(self.size())

    def __str__(self) -> str:
        return f"Queue: {self.__queue}"


class MyStack:
    def __init__(self):
        self.__pqueue = Queue()

    def push(self, x: int) -> None:
        self.__pqueue.enqueue(x)

    def pop(self) -> int:
        for _ in range(self.__pqueue.size() - 1):
            temp = self.__pqueue.dequeue()
            self.__pqueue.enqueue(temp)
        val = self.__pqueue.dequeue()
        return val

    def top(self) -> int:
        val = self.pop()
        self.__pqueue.enqueue(val)
        return val

    def empty(self) -> bool:
        return self.__pqueue.isEmpty()

    def __str__(self) -> str:
        return f"Stack: {self.__pqueue}"


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

if __name__ == "__main__":
    a = MyStack()
    a.push(1)
    a.push(2)
    assert a.top() == 2
    assert a.pop() == 2
    assert a.empty() == False

    print("Passed")
