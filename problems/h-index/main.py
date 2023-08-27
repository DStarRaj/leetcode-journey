class Solution:
    def hIndex(self, citations: list[int]) -> int:
        publishes = len(citations)
        citations.sort()
        for i in range(1, publishes + 1):
            h_count = 0
            for c in citations:
                if c >= i:
                    h_count += 1
                if h_count == i:
                    break
            if h_count < i:
                return i - 1
        return i


if __name__ == "__main__":
    test_cases = [
        [3, 0, 6, 1, 5],
        [1, 3, 1],
    ]
    test_results = [
        3,
        1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.hIndex(test) == result

    print("Passed")
