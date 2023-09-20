class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        target: int = sum(nums) - x
        curr_sum: int = 0
        L = 0
        max_win = -1
        for R in range(n):
            curr_sum += nums[R]

            while R >= L and curr_sum > target:
                curr_sum -= nums[L]
                L += 1

            if curr_sum == target:
                max_win = max(max_win, R - L + 1)

        return -1 if max_win == -1 else n - max_win


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 4, 2, 3], 5),
        ([5, 6, 7, 8, 9], 4),
        ([3, 2, 20, 1, 1, 3], 10),
    ]
    test_results = [
        2,
        -1,
        5,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minOperations(*test) == result

    print("Passed")
