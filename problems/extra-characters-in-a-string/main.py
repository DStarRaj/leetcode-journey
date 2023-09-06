class Solution:
    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        words = set(dictionary)
        dp = {len(s): 0}

        def min_words(index: int):
            if index in dp:
                return dp[index]
            min_skip = 1 + min_words(index + 1)
            for j in range(index, len(s)):
                if s[index : j + 1] in words:
                    min_skip = min(min_skip, min_words(j + 1))
            dp[index] = min_skip
            return min_skip

        return min_words(0)


if __name__ == "__main__":
    test_cases = [
        ("leetscode", ["leet", "code", "leetcode"]),
        ("sayhelloworld", ["hello", "world"]),
    ]
    test_results = [
        1,
        3,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minExtraChar(test[0], test[1]) == result

    print("Passed")
