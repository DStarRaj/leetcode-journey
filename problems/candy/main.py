class Solution:
    def candy(self, ratings: list[int]) -> int:
        ary = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                ary[i] = ary[i - 1] + 1

        total = 0
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                if ary[i] <= ary[i + 1]:
                    ary[i] = ary[i + 1] + 1
            total += ary[i]

        total += ary[-1]
        return total


if __name__ == "__main__":
    a = Solution()
    a.candy([1, 2, 2])
