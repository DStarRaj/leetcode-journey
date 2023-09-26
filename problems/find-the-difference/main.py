class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sord = 0
        tord = 0

        for each in s:
            sord += ord(each)

        for each in t:
            tord += ord(each)

        return chr(tord - sord)


if __name__ == "__main__":
    test_cases = [
        ("abcd", "abcde"),
        ("", "y"),
    ]
    test_results = [
        "e",
        "y",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findTheDifference(*test) == result

    print("Passed")
