from collections import defaultdict
from typing import List, Optional

class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to nodes
        self.left, self.right = Node(0,0), Node(0,0)
        
        # Left is LRU right is most recent
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        """Insert at right of doubly linked list (aka most recent)"""
        prev = self.right.prev
        next = self.right
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    
def main():
    lRUCache = LRUCache(2)
    print(lRUCache.put(1, 1)) # cache is {1=1}
    print(lRUCache.put(2, 2)) # cache is {1=1, 2=2}
    print(lRUCache.get(1)  )  # return 1
    print(lRUCache.put(3, 3)) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2)  )  # returns -1 (not found)
    print(lRUCache.put(4, 4)) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1)  )  # return -1 (not found)
    print(lRUCache.get(3)  )  # return 3
    print(lRUCache.get(4)  )  # return 4

if __name__ == "__main__":
    main()