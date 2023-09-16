class minHeap:
    def __init__(self) -> None:
        self.heap = []

    def __bool__(self) -> bool:
        return bool(len(self.heap))

    def __str__(self) -> str:
        return f"{self.heap}"

    def add(self, val) -> None:
        self.heap.append(val)
        self.heap.sort()

    def pop(self):
        return self.heap.pop(0)


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        row = len(heights)
        column = len(heights[0])
        effort_ary = [[float("inf")] * column for _ in range(row)]
        effort_ary[0][0] = 0
        heap = minHeap()
        heap.add([0, 0, 0])
        while heap:
            curr = heap.pop()
            right = [curr[1], curr[2] + 1]
            left = [curr[1], curr[2] - 1]
            up = [curr[1] - 1, curr[2]]
            down = [curr[1] + 1, curr[2]]

            if right[1] < column:
                cost = max(
                    curr[0],
                    abs(heights[curr[1]][curr[2]] - heights[right[0]][right[1]]),
                )
                if cost < effort_ary[right[0]][right[1]]:
                    effort_ary[right[0]][right[1]] = cost
                    heap.add([cost, right[0], right[1]])

            if down[0] < row:
                cost = max(
                    curr[0],
                    abs(heights[curr[1]][curr[2]] - heights[down[0]][down[1]]),
                )
                if cost < effort_ary[down[0]][down[1]]:
                    effort_ary[down[0]][down[1]] = cost
                    heap.add([cost, down[0], down[1]])

            if left[1] >= 0:
                cost = max(
                    curr[0],
                    abs(heights[curr[1]][curr[2]] - heights[left[0]][left[1]]),
                )
                if cost < effort_ary[left[0]][left[1]]:
                    effort_ary[left[0]][left[1]] = cost
                    heap.add([cost, left[0], left[1]])

            if up[0] >= 0:
                cost = max(
                    curr[0],
                    abs(heights[curr[1]][curr[2]] - heights[up[0]][up[1]]),
                )
                if cost < effort_ary[up[0]][up[1]]:
                    effort_ary[up[0]][up[1]] = cost
                    heap.add([cost, up[0], up[1]])

            if curr[1] == row - 1 and curr[2] == column - 1:
                break

        return effort_ary[-1][-1]


if __name__ == "__main__":
    test_cases = [
        [
            [1, 2, 2],
            [3, 8, 2],
            [5, 3, 5],
        ],
        [
            [1, 2, 3],
            [3, 8, 4],
            [5, 3, 5],
        ],
        [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1],
        ],
    ]
    test_results = [
        2,
        1,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minimumEffortPath(test) == result

    print("Passed")
