class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # counter for s
        j = 0  # counter for t
        l_s = len(s)
        l_t = len(t)
        while j < l_t:
            if s[i] == t[j]:
                i += 1
            if i == l_s:
                return True
            j += 1
        return False


if __name__ == "__main__":
    test_cases = [
        ("abc", "ahbgdc"),
        ("axc", "ahbgdc"),
    ]
    test_results = [
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isSubsequence(*test) == result

    print("Passed")
