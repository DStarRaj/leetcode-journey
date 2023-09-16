class Solution:
    def trap(self, height: list[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        L = 0
        R = len(height) - 1
        water = 0
        while L != R:
            if maxL < maxR:
                L += 1
                elevation = height[L]
                if maxL < elevation:
                    maxL = elevation
                water += maxL - elevation
            else:
                R -= 1
                elevation = height[R]
                if maxR < elevation:
                    maxR = elevation
                water += maxR - elevation
        return water


if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
    ]
    test_results = [
        6,
        9,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.trap(test) == result

    print("Passed")
