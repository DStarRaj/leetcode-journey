class Solution:
    def intToRoman(self, num: int) -> str:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        order = ["M", "D", "C", "L", "X", "V", "I"]
        roman = ""
        while num > 0:
            quo = num // mapping["C"]
            if quo == 4:
                roman += "CD"
                num -= quo * mapping["C"]
                continue
            if quo == 9:
                roman += "CM"
                num -= quo * mapping["C"]
                continue
            quo = num // mapping["X"]
            if quo == 4:
                roman += "XL"
                num -= quo * mapping["X"]
                continue
            if quo == 9:
                roman += "XC"
                num -= quo * mapping["X"]
                continue
            quo = num // mapping["I"]
            if quo == 4:
                roman += "IV"
                num -= quo * mapping["I"]
                continue
            if quo == 9:
                roman += "IX"
                num -= quo * mapping["I"]
                continue

            for each in order:
                quo = num // mapping[each]
                if quo:
                    roman += quo * each
                    num -= quo * mapping[each]
                    break

        return roman


if __name__ == "__main__":
    test_cases = [
        3,
        58,
        1994,
    ]
    test_results = [
        "III",
        "LVIII",
        "MCMXCIV",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.intToRoman(test) == result

    print("Passed")
