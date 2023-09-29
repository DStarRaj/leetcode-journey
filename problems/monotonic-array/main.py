class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        increasing = True
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                pass
            else:
                increasing = False
                break

        decreasing = True
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                pass
            else:
                decreasing = False
                break

        return increasing or decreasing


if __name__ == "__main__":
    test_cases = [
        [1, 2, 2, 3],
        [6, 5, 4, 4],
        [1, 3, 2],
    ]
    test_results = [
        True,
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isMonotonic(test) == result

    print("Passed")
