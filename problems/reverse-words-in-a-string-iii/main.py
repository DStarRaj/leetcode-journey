class Solution:
    def reverseWords(self, s: str) -> str:
        ary_s = []
        idx = 0
        for i, c in enumerate(s):
            if c != " ":
                ary_s.insert(idx, c)
            else:
                ary_s.append(c)
                idx = i + 1
        return "".join(ary_s)


if __name__ == "__main__":
    test_cases = [
        "Let's take LeetCode contest",
        "God Ding",
    ]
    test_results = [
        "s'teL ekat edoCteeL tsetnoc",
        "doG gniD",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.reverseWords(test) == result

    print("Passed")
