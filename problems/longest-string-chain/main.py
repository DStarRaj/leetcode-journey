class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        swords = set(words)
        memo = {}

        def wordChain(word):
            if word not in swords:
                return 0
            l = memo.get(word)
            if l:
                return l

            lword = len(word)
            mx = 0

            for i in range(lword):
                sub_word = word[:i] + word[i + 1 :]
                mx = max(mx, wordChain(sub_word) + 1)

            memo[word] = mx
            return mx

        for each in swords:
            wordChain(each)

        return max(memo.values())


if __name__ == "__main__":
    test_cases = [
        ["a", "b", "ba", "bca", "bda", "bdca"],
        ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"],
        ["abcd", "dbqca"],
    ]
    test_results = [
        4,
        5,
        1,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.longestStrChain(test) == result

    print("Passed")
