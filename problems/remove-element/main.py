class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
                continue
            i += 1

        return j + 1


if __name__ == "__main__":
    test_cases = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
    ]
    test_results = [
        ([2, 2], 2),
        ([0, 1, 4, 0, 3], 5),
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.removeElement(test[0], test[1]) == result[1]
        assert sorted(test[0][: result[1]]) == sorted(result[0])

    print("Passed")
