class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        sorted_s: list[int] = sorted(satisfaction, reverse=True)
        presum: int = 0
        result: int = 0
        for each in sorted_s:
            presum += each
            if presum >= 0:
                result += presum
            else:
                break
        return result


if __name__ == "__main__":
    test_cases = [
        [-1, -8, 0, 5, -9],
        [4, 3, 2],
        [-1, -4, -5],
    ]
    test_results = [
        14,
        20,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.maxSatisfaction(test) == result

    print("Passed")
