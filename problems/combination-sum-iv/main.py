class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        cache = {0: 1}

        for n in range(1, target + 1):
            ways = 0
            for each in nums:
                ways += cache.get(n - each, 0)
            cache[n] = ways

        return cache[target]


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 4),
        ([9], 3),
    ]
    test_results = [
        7,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.combinationSum4(*test) == result

    print("Passed")
