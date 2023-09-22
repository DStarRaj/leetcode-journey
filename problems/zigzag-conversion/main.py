class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ary = [[] for _ in range(numRows)]
        n = len(s)
        i = 0
        tracker = +1
        ary_counter = 0
        while i < n:
            ary[ary_counter].append(s[i])
            if numRows > 1:
                ary_counter += tracker
            if ary_counter == 0 or ary_counter == (numRows - 1):
                tracker *= -1
            i += 1
        ans = ""
        for each in ary:
            ans += "".join(each)
        return ans


if __name__ == "__main__":
    test_cases = [
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
    ]
    test_results = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.convert(*test) == result

    print("Passed")
