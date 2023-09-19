class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengthmap = {}
        for index, each in enumerate(mat):
            nsoldiers = each.count(1)
            strengthmap[index] = nsoldiers
        sorted_strength = sorted(strengthmap, key=lambda x: strengthmap[x])
        return sorted_strength[:k]


if __name__ == "__main__":
    test_cases = [
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
        ),
        (
            [
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
            ],
            2,
        ),
    ]
    test_results = [
        [2, 0, 3],
        [0, 2],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.kWeakestRows(*test) == result

    print("Passed")
