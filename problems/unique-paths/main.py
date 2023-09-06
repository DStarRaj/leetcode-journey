class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i, m_val in enumerate(dp):
            for j in range(len(m_val)):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    test_cases = [
        (3, 7),
        (3, 2),
    ]
    test_results = [
        28,
        3,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.uniquePaths(test[0], test[1]) == result

    print("Passed")
