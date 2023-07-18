from typing import List


class Solution:
    def __init__(self):
        self.GRAPH = []
        self.analysed_nodes = {}
        self.safe_nodes = []

    def is_safe(self, index):
        safe = self.analysed_nodes.get(index)
        if safe != None:
            return safe

        self.analysed_nodes[index] = False
        node = self.GRAPH[index]
        for path in node:
            pathIsSafe = self.is_safe(path)
            if not pathIsSafe:
                return pathIsSafe

        self.analysed_nodes[index] = True
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.GRAPH = graph

        for index, node in enumerate(graph):
            if self.is_safe(index):
                self.safe_nodes.append(index)

        return self.safe_nodes


if __name__ == "__main__":
    test_cases = [
        [[1, 2], [2, 3], [5], [0], [5], [], []],
        [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []],
    ]
    test_results = [
        [2, 4, 5, 6],
        [4],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.eventualSafeNodes(test) == result

    print("Passed")
