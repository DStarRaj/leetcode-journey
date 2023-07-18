class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        rev_num = 0

        if x < 0:
            return False

        while num >= 1:
            unit = num % 10
            num = num // 10
            rev_num = rev_num * 10 + unit

        if rev_num == x:
            return True
        return False


if __name__ == "__main__":
    test_cases = [
        121,
        -121,
        10,
    ]
    test_results = [
        True,
        False,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isPalindrome(test) == result

    print("Passed")
