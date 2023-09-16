class DisjointSet:
    def __init__(self) -> None:
        self.sets: list[list[int]] = []

    def makeset(self, val: int) -> None:
        self.sets.append([val])

    def findset(self, val: int) -> list[int]:
        for set in self.sets:
            for set_val in set:
                if set_val == val:
                    return set

    def __str__(self) -> str:
        return f"{self.sets}"

    def empty_set(self, set: list[int]) -> None:
        while set:
            set.pop()

    def union(self, valA: int, valB: int) -> bool:
        setA = self.findset(valA)
        setB = self.findset(valB)
        if setA == setB:
            return False
        for each in setB:
            setA.append(each)
        self.empty_set(setB)
        return True


class Solution:
    def abs(self, number: int) -> int:
        if number >= 0:
            return number
        return -number

    def manhattan_dist(self, pointA: list[int], pointB: list[int]) -> int:
        return self.abs(pointB[0] - pointA[0]) + self.abs(pointB[1] - pointA[1])

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        all_edges = []
        dset = DisjointSet()

        for i in range(N):
            for j in range(i + 1, N):
                dist = self.manhattan_dist(points[i], points[j])
                all_edges.append([dist, i, j])
            dset.makeset(i)

        all_edges.sort()

        res = 0
        edge_count = 0

        for dist, pointA, pointB in all_edges:
            if dset.union(pointA, pointB):
                res += dist
                edge_count += 1
            if edge_count == N - 1:
                break

        return res


if __name__ == "__main__":
    test_cases = [
        [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        [[3, 12], [-2, 5], [-4, 1]],
    ]
    test_results = [
        20,
        18,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minCostConnectPoints(test) == result

    print("Passed")
