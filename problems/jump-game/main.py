class Solution:
    def canJump(self, nums: list[int]) -> bool:
        ptr = len(nums) - 1
        i = ptr
        while i >= 0:
            if nums[i] + i >= ptr:
                ptr = i
            i -= 1

        if ptr == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
    ]
    test_results = [
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.canJump(test) == result

    print("Passed")
