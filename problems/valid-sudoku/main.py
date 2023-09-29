class Solution:
    def hasDuplicate(self, ary: list[str]):
        n = len(ary)
        s = set(ary)
        if n != len(s):
            return True
        return False

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        ## check for valid rows and columns
        for i in range(9):
            rary = []
            cary = []
            for j in range(9):
                rcell = board[i][j]
                if rcell != ".":
                    rary.append(rcell)

                ccell = board[j][i]
                if ccell != ".":
                    cary.append(ccell)

            if self.hasDuplicate(rary):
                return False

            if self.hasDuplicate(cary):
                return False

        ## check for valid squares
        for h in range(3):
            for i in range(3):
                ary = []
                for j in range(3):
                    for k in range(3):
                        cell = board[j + 3 * h][k + 3 * i]
                        if cell != ".":
                            ary.append(int(cell))
                if self.hasDuplicate(ary):
                    return False

        return True


if __name__ == "__main__":
    test_cases = [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
    ]
    test_results = [
        True,
        False,
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.isValidSudoku(test) == result

    print("Passed")
