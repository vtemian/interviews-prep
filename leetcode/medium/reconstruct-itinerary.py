from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        airports = defaultdict(list)
        result = []
        tickets.sort(reverse=True)

        for _to, _from in tickets:
            airports[_to].append(_from)

        stack = ['JFK']

        while stack:
            while airports[stack[-1]]:
                stack.append(airports[stack[-1]].pop())
            result.append(stack.pop())

        return result[::-1]
