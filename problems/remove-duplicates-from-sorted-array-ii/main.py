class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        m: int = 1
        flag = True
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[m] = nums[i]
                flag = True
                m += 1
            elif flag:
                nums[m] = nums[i]
                m += 1
                flag = False
        return m


if __name__ == "__main__":
    test_cases = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
    ]
    test_results = [
        ([1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 2, 3, 3], 7),
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.removeDuplicates(test) == result[1]
        assert test[: result[1]] == result[0]

    print("Passed")
