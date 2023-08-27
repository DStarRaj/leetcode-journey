class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i = 1
        profit = 0
        while i < len(prices):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
            i += 1
        return profit


if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [1, 2, 3, 4, 5],
        [7, 6, 4, 3, 1],
    ]
    test_results = [
        7,
        4,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.maxProfit(test) == result

    print("Passed")
