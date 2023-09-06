class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        intervals = []
        for i, val in enumerate(ranges):
            intervals.append([-val + i, val + i])
        intervals = sorted(intervals, key=lambda x: x[0])
        field = [0, n]
        taps = 0
        while True:
            coverage = 0
            coverage_area = []
            for each in intervals:
                e = min(each[1], field[1])
                s = max(each[0], field[0])
                cov = e - s
                if cov > coverage and s == field[0]:
                    coverage_area = [s, e]
                    coverage = cov
            if coverage_area:
                taps += 1
                remaining_field = [coverage_area[1], n]
                field = remaining_field
                if remaining_field[0] == remaining_field[1]:
                    break
            else:
                break
        if field[0] != field[1]:
            return -1
        return taps


if __name__ == "__main__":
    test_cases = [
        (5, [3, 4, 1, 1, 0, 0]),
        (3, [0, 0, 0, 0]),
    ]
    test_results = [
        1,
        -1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minTaps(test[0], test[1]) == result

    print("Passed")
