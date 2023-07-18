class Solution:
    def units(self, x: int) -> int:
        num = x
        r = 0
        while num > 0:
            r += 1
            num = num // 10
        return r

    def getlargenum(self, digit: int) -> int:
        largenum = "2147483647"
        return int(largenum[:digit])

    def abs(self, num: int) -> int:
        if num < 0:
            return -num
        return num

    def reverse(self, x: int) -> int:
        num = self.abs(x)
        unit = self.units(num)
        rev = 0
        while num > 0:
            rev = (rev * 10) + (num % 10)
            num = num // 10
            if unit >= 10:
                rev_unit = self.units(rev)
                if rev > self.getlargenum(rev_unit):
                    return 0

        if x < 0:
            rev = -rev

        return rev


if __name__ == "__main__":
    test_cases = [
        123,
        -123,
        120,
    ]
    test_results = [
        321,
        -321,
        21,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.reverse(test) == result

    print("Passed")
