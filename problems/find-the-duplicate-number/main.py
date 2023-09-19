class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow2 = slow1 = fast = 0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break
        while True:
            if slow1 == slow2:
                return slow1
            slow1 = nums[slow1]
            slow2 = nums[slow2]


if __name__ == "__main__":
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
    ]
    test_results = [
        2,
        3,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findDuplicate(test) == result

    print("Passed")
