from typing import List


class Solution:
    def __init__(self) -> None:
        self.GRAPH = {}
        self.visited = {}
        self.recStack = {}

    def is_Cyclic(self, index) -> bool:
        self.visited[index] = True
        self.recStack[index] = True
        for node in self.GRAPH[index]:
            if self.visited.get(node):
                if self.recStack[node]:
                    return True
            else:
                if self.is_Cyclic(node):
                    return True
        self.recStack[index] = False
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for node in range(numCourses):
            self.GRAPH[node] = []

        for direction in prerequisites:
            self.GRAPH[direction[0]].append(direction[1])

        for node in self.GRAPH:
            if not self.visited.get(node):
                if self.is_Cyclic(node):
                    return False

        return True


if __name__ == "__main__":
    test_cases = [
        (2, [[1, 0]]),
        (2, [[1, 0], [0, 1]]),
    ]
    test_results = [
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.canFinish(numCourses=test[0], prerequisites=test[1]) == result

    print("Passed")
