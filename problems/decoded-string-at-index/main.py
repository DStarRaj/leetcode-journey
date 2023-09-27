class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoder = [1]
        for c in s[1:]:
            casc = ord(c)
            if casc >= 50 and casc <= 57:
                c = int(c)
                decoder.append(decoder[-1] * c)
            else:
                decoder.append(decoder[-1] + 1)

        sub_k = k
        for i, dec in enumerate(decoder[::-1]):
            if sub_k == dec:
                index = i
                break
            elif sub_k < dec:
                continue
            else:
                sub_k = sub_k % dec
                if sub_k == 0:
                    index = i
                    break

        pindex = len(s) - index - 1
        while True:
            casc = ord(s[pindex])
            if casc >= 50 and casc <= 57:
                pindex -= 1
            else:
                break
        return s[pindex]


if __name__ == "__main__":
    test_cases = [
        ("leet2code3", 10),
        ("ha22", 5),
        ("a2345678999999999999999", 1),
    ]
    test_results = [
        "o",
        "h",
        "a",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.decodeAtIndex(*test) == result

    print("Passed")
