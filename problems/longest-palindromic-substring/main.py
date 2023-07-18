class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        palin = ""
        dp = [[0] * l for _ in range(l)]

        for length in range(l):
            for i in range(l):
                j = i + length
                if j >= l:
                    break

                if length == 0:
                    dp[i][j] = 1
                    palin = s[i : j + 1]
                elif length == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        palin = s[i : j + 1]
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                        dp[i][j] = 1
                        palin = s[i : j + 1]

        return palin


if __name__ == "__main__":
    test_cases = [
        "babad",
        "cbbd",
    ]
    test_results = [
        ["bab", "aba"],
        ["bb"],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        solutions = []
        for res in result:
            solutions.append(
                a.longestPalindrome(test) == res
            )
        assert any(solutions)

    print("Passed")
