class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        if not pairs:
            return 0

        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        dp = [1] * len(sorted_pairs)

        for i in range(1, len(sorted_pairs)):
            for j in range(i):
                if sorted_pairs[i][0] > sorted_pairs[j][1] and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1

        return max(dp)


if __name__ == "__main__":
    test_cases = [
        [[1, 2], [2, 3], [3, 4]],
        [[1, 2], [7, 8], [4, 5]],
        [[-10, -8], [8, 9], [-5, 0], [6, 10], [-6, -4], [1, 7], [9, 10], [-4, 7]],
    ]
    test_results = [
        2,
        3,
        4,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findLongestChain(test) == result

    print("Passed")
