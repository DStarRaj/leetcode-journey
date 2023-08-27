class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        ptr_l = ptr_r = 0
        while ptr_r < len(nums) - 1:
            max_jump = 0
            for i in range(ptr_l, ptr_r + 1):
                max_jump = max(max_jump, i + nums[i])
            ptr_l = ptr_r + 1
            ptr_r = max_jump
            jumps += 1
        return jumps


if __name__ == "__main__":
    test_cases = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
    ]
    test_results = [
        2,
        2,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.jump(test) == result

    print("Passed")
