class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers_l = len(customers)
        penalties = [0]
        for i in range(1, customers_l + 1):
            penalties.append(penalties[i - 1])
            if customers[i - 1] == "N":
                penalties[i] += 1
        postfix_Y = 0
        for i in range(customers_l - 1, -1, -1):
            if customers[i] == "Y":
                postfix_Y += 1
            penalties[i] += postfix_Y
        return penalties.index(min(penalties))


if __name__ == "__main__":
    test_cases = [
        "YYNY",
        "NNNNN",
        "YYYY",
    ]
    test_results = [
        2,
        0,
        4,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.bestClosingTime(test) == result

    print("Passed")
