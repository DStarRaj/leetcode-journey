from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        ans = 1
        for i in range(n):
            num = arr[i]
            search_item = num - difference
            if search_item in dp:
                dp[num] = dp[search_item] + 1
            else:
                dp[num] = 1
            ans = max(ans, dp[num])
        return ans


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 1),
        ([1, 3, 5, 7], 1),
        ([1, 5, 7, 8, 5, 3, 4, 2, 1], -2),
        ([4, 12, 10, 0, -2, 7, -8, 9, -9, -12, -12, 8, 8], 0),
    ]
    test_results = [
        4,
        1,
        4,
        2,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.longestSubsequence(arr=test[0], difference=test[1]) == result

    print("Passed")
