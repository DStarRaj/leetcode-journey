class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pos = []
        for i, each in enumerate(s):
            if each in t:
                pos.append(i)

        thm = {}
        nhm = {}

        for each in t:
            val = thm.setdefault(each, 0)
            thm[each] = val + 1
            nhm.setdefault(each, 0)

        need = len(thm)
        have = 0

        leng = float("inf")
        minwin = ""

        L = 0
        for R in range(len(pos)):
            chr = s[pos[R]]
            nhm[chr] += 1
            if nhm[chr] == thm[chr]:
                have += 1

            if have == need:
                nleng = pos[R] - pos[L] + 1
                if nleng < leng:
                    leng = nleng
                    minwin = s[pos[L] : pos[R] + 1]

                while have == need:
                    prechr = s[pos[L]]
                    nhm[prechr] -= 1
                    if nhm[prechr] < thm[prechr]:
                        have -= 1
                    L += 1

                    if have == need:
                        nleng = pos[R] - pos[L] + 1
                        if nleng < leng:
                            leng = nleng
                            minwin = s[pos[L] : pos[R] + 1]

        return minwin


if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
    ]
    test_results = [
        "BANC",
        "a",
        "",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minWindow(*test) == result

    print("Passed")
