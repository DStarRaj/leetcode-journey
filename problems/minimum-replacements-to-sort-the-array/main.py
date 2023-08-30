class Solution:
    def ceil(self, val: float) -> int:
        if int(val) < val:
            return int(val) + 1
        else:
            return int(val)

    def minimumReplacement(self, nums: list[int]) -> int:
        ptr_r = nums[-1]
        replaces = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > ptr_r:
                splits = self.ceil(nums[i] / ptr_r)
                replaces += splits - 1
                ptr_r = nums[i] // splits
            else:
                ptr_r = nums[i]
        return replaces


if __name__ == "__main__":
    test_cases = [
        [3, 9, 3],
        [1, 2, 3, 4, 5],
    ]
    test_results = [
        2,
        0,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minimumReplacement(test) == result

    print("Passed")
