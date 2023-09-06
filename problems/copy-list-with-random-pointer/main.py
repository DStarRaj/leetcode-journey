# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None
        hash_map = {}
        curr = head
        while curr != None:
            new = Node(curr.val)
            hash_map[curr] = new
            curr = curr.next
        for old, new in hash_map.items():
            if old.next:
                new.next = hash_map[old.next]
            if old.random:
                new.random = hash_map[old.random]
        return hash_map[head]
