from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if other == None:
            return False

        a = self
        b = other
        a_arr = []
        b_arr = []
        while a != None:
            a_arr.append(a.val)
            a = a.next
        while b != None:
            b_arr.append(b.val)
            b = b.next
        return a_arr == b_arr


class Solution:
    @staticmethod
    def linklist_to_num(list: ListNode) -> int:
        a = list
        num = 0
        while a != None:
            num = num * 10 + a.val
            a = a.next
        return num

    @staticmethod
    def list_to_linklist(arr: list) -> ListNode:
        root = None
        curr = None
        prev = None
        for each in arr:
            if root == None:
                root = ListNode(val=each)
                curr = root
            else:
                curr = ListNode(val=each)
                prev.next = curr
            prev = curr
        return root

    def num_to_linklist(self, num: int) -> ListNode:
        num_copy = num
        nums = []
        while num_copy > 0:
            nums.insert(0, num_copy % 10)
            num_copy = num_copy // 10
        if num == 0 and nums == []:
            nums = [0]

        return self.list_to_linklist(nums)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.linklist_to_num(l1)
        num2 = self.linklist_to_num(l2)
        return self.num_to_linklist(num1 + num2)


def contrustLinkList(arr: list):
    root = None
    curr = None
    prev = None
    for each in arr:
        if root == None:
            root = ListNode(val=each)
            curr = root
        else:
            curr = ListNode(val=each)
            prev.next = curr
        prev = curr
    return root


def printLinkList(list: ListNode):
    node = list
    while node != None:
        print(node.val)
        node = node.next


if __name__ == "__main__":
    test_cases = [
        (contrustLinkList([7, 2, 4, 3]), contrustLinkList([5, 6, 4])),
        (contrustLinkList([2, 4, 3]), contrustLinkList([5, 6, 4])),
        (contrustLinkList([0]), contrustLinkList([0])),
    ]
    test_results = [
        contrustLinkList([7, 8, 0, 7]),
        contrustLinkList([8, 0, 7]),
        contrustLinkList([0]),
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.addTwoNumbers(test[0], test[1]) == result

    print("Passed")
