class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # head -> node -> tail
    # prev <-      <- next
    def remove(self, node):
        node_next, node_prev = node.next, node.prev
        node_prev.next = node_next
        node_next.prev = node_prev

    # head -> insert -> tail
    # prev <-      <- next
    def insert(self, node):
        node.next, node.prev = self.tail, self.tail.prev
        node.prev.next = self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return

        if len(self.cache) == self.capacity:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])