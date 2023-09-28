class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        prehm = {}
        for each in words:
            val = prehm.setdefault(each, 0)
            prehm[each] = val + 1

        ns = len(s)
        nwords = len(words)
        nchip = len(words[0])

        indexes = []

        winsize = nwords * nchip
        for L in range(ns - winsize + 1):
            window = s[L : L + winsize]
            temphm = {}
            for sub in range(0, len(window), nchip):
                subword = window[sub : nchip + sub]
                val = temphm.setdefault(subword, 0)
                temphm[subword] = val + 1
            if temphm == prehm:
                indexes.append(L)

        return indexes


if __name__ == "__main__":
    test_cases = [
        ("barfoothefoobarman", ["foo", "bar"]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
    ]
    test_results = [
        [0, 9],
        [],
        [6, 9, 12],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findSubstring(*test) == result

    print("Passed")
