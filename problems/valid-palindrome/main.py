class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        L = 0
        R = n - 1
        mtch = True
        while L < R:
            sL = s[L]
            sR = s[R]
            if not sL.isalnum():
                L += 1
            elif not sR.isalnum():
                R -= 1
            else:
                if sL.lower() == sR.lower():
                    L += 1
                    R -= 1
                    continue
                else:
                    mtch = False
                    break
        return mtch


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
    ]
    test_results = [
        True,
        False,
        True,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isPalindrome(test) == result

    print("Passed")
