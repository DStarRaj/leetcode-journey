class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        L, ttsum = 0, 0
        n = len(nums)
        res = n + 1

        for R in range(n):
            ttsum += nums[R]
            while ttsum >= target:
                res = min(res, R - L + 1)
                ttsum -= nums[L]
                L += 1

        return 0 if res == n + 1 else res


if __name__ == "__main__":
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3]),
        (4, [1, 4, 4]),
        (11, [1, 1, 1, 1, 1, 1, 1, 1]),
    ]
    test_results = [
        2,
        1,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minSubArrayLen(*test) == result

    print("Passed")
