class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # intermediate = []
        possible = 0
        total = 0
        res = 0
        for i in range(len(gas)):
            save = gas[i] - cost[i]
            possible += save
            total += save
            if total < 0:
                total = 0
                res = i + 1
            # intermediate.append(save)

        # print(intermediate)
        if possible >= 0:
            return res
        return -1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        ([2, 3, 4], [3, 4, 3]),
    ]
    test_results = [
        3,
        -1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.canCompleteCircuit(test[0], test[1]) == result

    print("Passed")
