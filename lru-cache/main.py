class Node:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.Head = None
        self.Tail = None
        self.cap = capacity
        self.curr = None
        self.hash = {}

    def get(self, key: int) -> int:
        self.curr = self.Head
        val = -1

        node = self.hash.get(key)
        if node:
            self.curr = node
            val = self.curr.value

        if val != -1:
            p = self.curr.prev
            n = self.curr.next
            if n:
                if p:
                    p.next = n
                    n.prev = p
                else:
                    n.prev = None
                    self.Head = n

                self.Tail.next = self.curr
                self.curr.prev = self.Tail
                self.curr.next = None
                self.Tail = self.curr

        return val

    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val != -1:
            self.curr.value = value
        else:
            if self.Head == None:
                self.Head = self.Tail = Node(key, value)
                self.hash[key] = self.Tail
                self.cap -= 1
            else:
                new_node = Node(key, value)
                self.hash[key] = new_node
                self.Tail.next = new_node
                new_node.prev = self.Tail
                self.Tail = new_node
                self.cap -= 1
            if self.cap < 0:
                node = self.Head
                self.Head = node.next
                self.Head.prev = None
                self.hash.pop(node.key)
                del node
                self.cap += 1


if __name__ == "__main__":
    lru = LRUCache(2)
    print(lru.get(2))
    lru.put(2, 6)
    print(lru.get(1))
    lru.put(1, 5)
    lru.put(1, 2)
    print(lru.get(1))
    print(lru.get(2))
