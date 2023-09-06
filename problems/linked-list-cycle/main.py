# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def contrustLinkList(arr: list, tail_point: int):
    root = None
    curr = None
    prev = None
    tail_pointer = None
    for index, each in enumerate(arr):
        if root == None:
            root = ListNode(each)
            curr = root
        else:
            curr = ListNode(each)
            prev.next = curr
        if index == tail_point:
            tail_pointer = curr
        prev = curr
    if tail_pointer:
        curr.next = tail_pointer
    return root


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        curr = head
        visited = []
        while curr != None:
            if curr in visited:
                return True
            visited.append(curr)
            curr = curr.next
        return False


if __name__ == "__main__":
    test_cases = [
        contrustLinkList([3, 2, 0, -4], 1),
        contrustLinkList([1, 2], 0),
        contrustLinkList([1], -1),
    ]
    test_results = [
        True,
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.hasCycle(test) == result

    print("Passed")
