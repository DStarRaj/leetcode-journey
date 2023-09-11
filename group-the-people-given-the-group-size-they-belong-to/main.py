class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        group = {}
        for index, group_size in enumerate(groupSizes):
            people_group: list[list[int]] = group.setdefault(group_size, [[]])
            if len(people_group[-1]) >= group_size:
                people_group.append([index])
            else:
                people_group[-1].append(index)

        end_group = []

        for people_groups in group.values():
            end_group.extend(people_groups)

        return end_group


if __name__ == "__main__":
    test_cases = [
        [3, 3, 3, 3, 3, 1, 3],
        [2, 1, 3, 3, 3, 2],
    ]
    test_results = [
        [[5], [0, 1, 2], [3, 4, 6]],
        [[1], [0, 5], [2, 3, 4]],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert sorted(a.groupThePeople(test)) == sorted(result)

    print("Passed")
