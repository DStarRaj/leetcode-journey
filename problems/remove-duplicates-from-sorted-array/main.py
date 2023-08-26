class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m: int = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[m] = nums[i]
                m += 1
        return m


if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    ]
    test_results = [
        ([1, 2], 2),
        ([0, 1, 2, 3, 4], 5),
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.removeDuplicates(test) == result[1]
        assert sorted(test[: result[1]]) == sorted(result[0])

    print("Passed")
