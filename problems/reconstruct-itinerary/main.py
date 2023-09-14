class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        routes = {}
        tickets.sort()
        for each in tickets:
            dest = routes.setdefault(each[0], [])
            dest.append(each[1])

        itenary = ["JFK"]

        def dfs(src):
            if len(itenary) == len(tickets) + 1:
                return True
            if src not in routes:
                return False

            temp = list(routes[src])
            for index, dest in enumerate(temp):
                routes[src].pop(index)
                itenary.append(dest)
                if dfs(dest):
                    return True
                itenary.pop()
                routes[src].insert(index, dest)
            return False

        dfs("JFK")

        return itenary


if __name__ == "__main__":
    test_cases = [
        [
            ["MUC", "LHR"],
            ["JFK", "MUC"],
            ["SFO", "SJC"],
            ["LHR", "SFO"],
        ],
        [
            ["JFK", "SFO"],
            ["JFK", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "JFK"],
            ["ATL", "SFO"],
        ],
    ]
    test_results = [
        ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
    ]

    for test, result in zip(test_cases, test_results):
        a = Solution()
        assert a.findItinerary(test) == result

    print("Passed")
