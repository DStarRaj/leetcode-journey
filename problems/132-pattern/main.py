class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack: list[list[int]] = []
        curMin = nums[0]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()

            if stack and stack[-1][1] < n:
                return True

            stack.append([n, curMin])
            curMin = min(n, curMin)

        return False


if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4],
        [3, 1, 4, 2],
        [-1, 3, 2, 0],
    ]
    test_results = [
        False,
        True,
        True,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.find132pattern(test) == result

    print("Passed")
