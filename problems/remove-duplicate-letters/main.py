class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        smap = {}
        for i, c in enumerate(s):
            smap[c] = i

        stack = []

        for i, c in enumerate(s):
            if c not in stack:
                ## check pre element if it is increasing or not
                while True:
                    if stack:
                        pre = stack[-1]
                        if pre < c:
                            stack.append(c)
                            break
                        else:
                            if smap[pre] > i:
                                stack.pop(-1)
                            else:
                                stack.append(c)
                                break
                    else:
                        stack.append(c)
                        break

        return "".join(stack)


if __name__ == "__main__":
    test_cases = [
        "bcabc",
        "cbacdcbc",
    ]
    test_results = [
        "abc",
        "acdb",
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.removeDuplicateLetters(test) == result

    print("Passed")
