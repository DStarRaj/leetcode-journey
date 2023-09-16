class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        number = 0
        prev = ""
        for curr in s:
            number += mapping[curr]
            if (curr == "V" or curr == "X") and prev == "I":
                number -= 2 * mapping["I"]
            if (curr == "L" or curr == "C") and prev == "X":
                number -= 2 * mapping["X"]
            if (curr == "D" or curr == "M") and prev == "C":
                number -= 2 * mapping["C"]
            prev = curr

        return number


if __name__ == "__main__":
    test_cases = [
        "III",
        "LVIII",
        "MCMXCIV",
    ]
    test_results = [
        3,
        58,
        1994,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.romanToInt(test) == result

    print("Passed")
