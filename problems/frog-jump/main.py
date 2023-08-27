class Solution:
    def canCross(self, stones: list[int]) -> bool:
        dp = {}
        for each in stones:
            dp[each] = set()
        dp[stones[0]].add(0)

        for stone in stones:
            for val in dp.get(stone):
                km = stone + val - 1
                k = stone + val
                kp = stone + val + 1
                if val - 1 > 0:
                    if dp.get(km) != None:
                        dp[km].add(val - 1)
                if val > 0:
                    if dp.get(k) != None:
                        dp[k].add(val)
                if dp.get(kp) != None:
                    dp[kp].add(val + 1)

        return True if len(dp.get(stones[-1])) else False


if __name__ == "__main__":
    test_cases = [
        [0, 1, 3, 5, 6, 8, 12, 17],
        [0, 1, 2, 3, 4, 8, 9, 11],
    ]
    test_results = [
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.canCross(test) == result

    print("Passed")
