class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[list[int]]:
        L = 0
        R = len(numbers) - 1
        ans = []
        while L < R:
            s = numbers[L] + numbers[R]
            if s < -target:
                L += 1
            elif s > -target:
                R -= 1
            else:
                sol = [target, numbers[L], numbers[R]]
                if sol not in ans:
                    ans.append(sol)
                L += 1
        return ans

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        snums = sorted(nums)
        prev = None
        for i, a in enumerate(snums[:-2]):
            if a == prev:
                continue
            prev = a
            com = self.twoSum(snums[i + 1 :], a)
            if com:
                res.extend(com)
        return res


if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
    ]
    test_results = [
        [[-1, -1, 2], [-1, 0, 1]],
        [],
        [[0, 0, 0]],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.threeSum(test) == result

    print("Passed")
