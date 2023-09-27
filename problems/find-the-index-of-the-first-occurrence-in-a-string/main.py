class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        h_l = len(haystack)
        for h_i in range(h_l):
            x = 0
            mtch = True
            for n in needle:
                h_x = x + h_i
                if h_x < h_l and haystack[x + h_i] == n:
                    x += 1
                else:
                    mtch = False
                    break
            if mtch == True:
                break

        if mtch:
            index = h_i

        return index


if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
    ]
    test_results = [
        0,
        -1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.strStr(*test) == result

    print("Passed")
