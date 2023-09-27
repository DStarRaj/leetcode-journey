class Solution:
    def maxArea(self, height: list[int]) -> int:
        L = 0
        n = len(height)
        R = n - 1
        area = 0
        while L < R:
            temp = (R - L) * min(height[L], height[R])
            if temp > area:
                area = temp

            if height[R] < height[L]:
                R -= 1
            else:
                L += 1

        return area


if __name__ == "__main__":
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
    ]
    test_results = [
        49,
        1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.maxArea(test) == result

    print("Passed")
