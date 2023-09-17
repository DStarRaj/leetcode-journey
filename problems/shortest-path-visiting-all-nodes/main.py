class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        n = len(graph)
        shortestPath = float("inf")
        aimState = (1 << n) - 1
        for i in range(n):
            queue = [(i, (1 << i))]
            seen = set(queue)
            lvl = 0
            while queue:
                if aimState in [x for _, x in queue]:
                    shortestPath = min(shortestPath, lvl)
                    break
                temp = []
                for u, visitedState in queue:
                    for v in graph[u]:
                        newState = (v, visitedState | (1 << v))
                        if newState not in seen:
                            temp.append(newState)
                            seen.add(newState)
                queue = temp
                lvl += 1
        return shortestPath


if __name__ == "__main__":
    test_cases = [
        [[1, 2, 3], [0], [0], [0]],
        [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]],
    ]
    test_results = [
        4,
        4,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.shortestPathLength(test) == result

    print("Passed")
