import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = {}
        hmap = collections.Counter(s)

        deletions = 0
        count_ary = set()

        for count in hmap.values():
            while count in count_ary:
                count -= 1
                deletions += 1

            if count != 0:
                count_ary.add(count)

        return deletions


if __name__ == "__main__":
    test_cases = [
        "aab",
        "aaabbbcc",
        "ceabaacb",
    ]
    test_results = [
        0,
        2,
        2,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.minDeletions(test) == result

    print("Passed")
