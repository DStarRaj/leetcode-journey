class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dp = {}
        for i in nums:
            dp[i] = dp.setdefault(i, 0) + 1
        for each in dp:
            if dp[each] > len(nums) // 2:
                return each


if __name__ == "__main__":
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
    ]
    test_results = [
        3,
        2,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.majorityElement(test) == result

    print("Passed")
