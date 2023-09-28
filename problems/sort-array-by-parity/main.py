class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        L = 0
        for R in range(len(nums)):
            if nums[R] % 2 == 0:
                t = nums[L]
                nums[L] = nums[R]
                nums[R] = t
                L += 1
        return nums


if __name__ == "__main__":
    test_cases = [
        [3, 1, 2, 4],
        [0],
    ]
    test_results = [
        [2, 4, 3, 1],
        [0],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.sortArrayByParity(test) == result

    print("Passed")
