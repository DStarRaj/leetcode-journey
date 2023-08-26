class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                if profit > maxP:
                    maxP = profit
            else:
                l = r
            r += 1
        return maxP


if __name__ == "__main__":
    test_cases = [
        [7, 1, 5, 3, 6, 4],
        [7, 6, 4, 3, 1],
    ]
    test_results = [
        5,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.maxProfit(test) == result

    print("Passed")
