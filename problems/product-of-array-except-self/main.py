class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        answer = [1]
        fix = nums[0]
        for i in range(1, l):
            answer.append(fix)
            fix *= nums[i]

        fix = nums[l - 1]
        for i in range(l - 2, -1, -1):
            answer[i] *= fix
            fix *= nums[i]

        return answer


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [-1, 1, 0, -3, 3],
    ]
    test_results = [
        [24, 12, 8, 6],
        [0, 0, 9, 0, 0],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.productExceptSelf(test) == result

    print("Passed")
