class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        ct = [[0 for x in range(x)] for x in range(1, query_row + 3)]
        ct[0][0] = poured
        for i in range(query_row):
            for j in range(len(ct[i])):
                overflow = (ct[i][j] - 1) / 2
                if overflow > 0:
                    ct[i][j] = 1
                    ct[i + 1][j] += overflow
                    ct[i + 1][j + 1] += overflow
        val = ct[query_row][query_glass]
        return val if val < 1 else 1


if __name__ == "__main__":
    test_cases = [
        (1, 1, 1),
        (2, 1, 1),
        (100000009, 33, 17),
    ]
    test_results = [
        0,
        0.5,
        1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.champagneTower(*test) == result

    print("Passed")
