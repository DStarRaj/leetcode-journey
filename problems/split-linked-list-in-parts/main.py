# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def len_list(self, head: ListNode) -> int:
        len = 0
        curr = head
        while curr != None:
            len += 1
            curr = curr.next
        return len

    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        length = self.len_list(head)
        quo = length // k
        rem = length % k
        list_of_nodes = []
        prev = None
        curr = head
        for _ in range(k):
            split = quo
            if rem > 0:
                split += 1
                rem -= 1
            part_head = None
            for x in range(split):
                if curr != None:
                    new = ListNode(curr.val)
                    if part_head == None:
                        part_head = new
                    if prev:
                        prev.next = new
                    prev = new
                    curr = curr.next
            list_of_nodes.append(part_head)
            prev = None
        return list_of_nodes
