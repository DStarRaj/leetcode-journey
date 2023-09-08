class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        starting = [[1]]
        for row in range(numRows - 1):
            temp_ary = [1]
            ## process
            for i in range(row):
                temp_ary.append(starting[-1][i] + starting[-1][i + 1])
            temp_ary.append(1)
            starting.append(temp_ary)
        return starting


if __name__ == "__main__":
    test_cases = [
        5,
        1,
    ]
    test_results = [
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]],
        [[1]],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.generate(test) == result

    print("Passed")
