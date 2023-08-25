class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        matrix = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        matrix[0][0] = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if not matrix[i][j]:
                    if j and s3[i + j - 1] == s2[j - 1] and matrix[i][j - 1]:
                        matrix[i][j] = 1
                        continue
                    if i and s3[i + j - 1] == s1[i - 1] and matrix[i - 1][j]:
                        matrix[i][j] = 1

        return bool(matrix[len(s1)][len(s2)])


if __name__ == "__main__":
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", ""),
        (
            "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc",
            "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb",
            "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb",
        ),
    ]
    test_results = [True, False, True, True]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isInterleave(test[0], test[1], test[2]) == result

    print("Passed")
