class Solution:
    def countOrders(self, n: int) -> int:
        total_pos = n * 2
        answer = 1
        while total_pos > 0:
            choices = (total_pos * (total_pos - 1)) // 2
            answer *= choices
            total_pos -= 2
        return answer % (10**9 + 7)


if __name__ == "__main__":
    test_cases = [
        1,
        2,
        3,
    ]
    test_results = [
        1,
        6,
        90,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.countOrders(test) == result

    print("Passed")
