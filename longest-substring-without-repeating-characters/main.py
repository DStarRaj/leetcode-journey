class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        max_length = 0
        for i, char in enumerate(s):
            if i <= length - max_length - 1:
                sub_arr = s[i+1: ]
                substr = char
                for each in sub_arr:
                    if each not in substr:
                        substr += each
                    else:
                        break
                l_substr = len(substr)
                if l_substr > max_length:
                    max_length = l_substr

        return max_length


if __name__ == "__main__":
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
    ]
    test_results = [
        3,
        1,
        3,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.lengthOfLongestSubstring(test) == result

    print("Passed")