class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_l = len(nums)
        if k >= nums_l:
            k = k % nums_l

        # reverse array full
        i = nums_l - 1
        j = 0
        while i > j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i -= 1
            j += 1

        # reverse k elements
        i = k - 1
        j = 0
        while i > j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i -= 1
            j += 1

        # reverse remaining elements
        i = nums_l - 1
        j = k
        while i > j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i -= 1
            j += 1


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([-1, -100, 3, 99], 2),
    ]
    test_results = [
        [5, 6, 7, 1, 2, 3, 4],
        [3, 99, -1, -100],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        a.rotate(test[0], test[1])
        assert test[0] == result

    print("Passed")
