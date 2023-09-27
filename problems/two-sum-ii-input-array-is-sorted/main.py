class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            s = numbers[L] + numbers[R]
            if s < target:
                L += 1
            elif s > target:
                R -= 1
            else:
                return [L + 1, R + 1]
        return []


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
    ]
    test_results = [
        [1, 2],
        [1, 3],
        [1, 2],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.twoSum(*test) == result

    print("Passed")
