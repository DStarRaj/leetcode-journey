class Solution:
    def line_length(self, line: list[str]) -> int:
        length = 0
        for each in line:
            length += len(each)
        length += len(line) - 1
        return length

    def justify_line(self, line: list[str], maxWidth: int, isLast=False) -> str:
        n_words = len(line)

        remaining_width = maxWidth - self.line_length(line)
        if n_words > 1:
            remain_divide = remaining_width // (n_words - 1)
        else:
            remain_divide = remaining_width
        remain_mod = remaining_width - remain_divide * (n_words - 1)

        justified_str = ""
        if isLast:
            for index, each in enumerate(line):
                if not (index == n_words - 1):
                    justified_str += each + " "
                else:
                    justified_str += each
            justified_str += " " * (maxWidth - len(justified_str))
        else:
            if n_words > 1:
                for index, each in enumerate(line):
                    if not (index != 0 and index == n_words - 1):
                        justified_str += each + " " * (1 + remain_divide)
                        if remain_mod:
                            justified_str += " "
                            remain_mod -= 1
                    else:
                        justified_str += each
            else:
                justified_str += line[0] + " " * remain_divide
        return justified_str

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        lines: list[list[str]] = []

        # Divide in lines
        i: int = 0
        while i < len(words):
            line: list[str] = []
            b: bool = True
            for j in range(i, len(words)):
                line.append(words[j])
                if self.line_length(line) > maxWidth:
                    line = line[:-1]
                    b = False
                    break
            lines.append(line)
            if b:
                break
            else:
                i = j

        # Justify lines
        justified_lines = []
        for index, each in enumerate(lines):
            justified_lines.append(
                self.justify_line(
                    each,
                    maxWidth,
                    isLast=(True if index == (len(lines) - 1) else False),
                )
            )
        return justified_lines


if __name__ == "__main__":
    test_cases = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What", "must", "be", "acknowledgment", "shall", "be"], 16),
        (
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        ),
        (["a"], 1),
    ]
    test_results = [
        ["This    is    an", "example  of text", "justification.  "],
        ["What   must   be", "acknowledgment  ", "shall be        "],
        [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  ",
        ],
        ["a"],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.fullJustify(words=test[0], maxWidth=test[1]) == result

    print("Passed")
