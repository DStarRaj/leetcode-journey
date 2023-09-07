# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        curr = head
        i = 1
        prev_link = None
        prev_curr = None
        rev_tail = None  # acts as start of the original link list
        rev_curr = None  # acts as end of the original link list
        end_link = None
        end_curr = None
        while curr != None:
            if i < left:
                new_node = ListNode(curr.val)
                if prev_link == None:
                    prev_link = new_node
                    prev_curr = new_node
                else:
                    prev_curr.next = new_node
                    prev_curr = new_node
            elif i <= right:
                new_node = ListNode(curr.val)
                if rev_tail == None:
                    rev_tail = new_node
                    rev_curr = new_node
                else:
                    new_node.next = rev_curr
                    rev_curr = new_node
            else:
                new_node = ListNode(curr.val)
                if end_link == None:
                    end_link = new_node
                    end_curr = new_node
                else:
                    end_curr.next = new_node
                    end_curr = new_node
            curr = curr.next
            i += 1
        if prev_curr:
            prev_curr.next = rev_curr
        if prev_link == None:
            prev_link = rev_curr
        rev_tail.next = end_link
        return prev_link
