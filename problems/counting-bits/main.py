class Solution:
    def countBits(self, n: int) -> list[int]:
        arr = [0, 1]

        while True:
            temp = []
            for i in arr:
                temp.append(i + 1)
            arr.extend(temp)
            if len(arr) > n:
                break

        return arr[: n + 1]


if __name__ == "__main__":
    test_cases = [
        2,
        5,
    ]
    test_results = [
        [0, 1, 1],
        [0, 1, 1, 2, 1, 2],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.countBits(test) == result

    print("Passed")
