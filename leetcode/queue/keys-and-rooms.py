class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        r = [0]

        while r:
            room = r.pop(0)
            if visited[room]:
                continue

            for rr in rooms[room]:
                if visited[rr]:
                    continue

                r.append(rr)
            visited[room] = 1

        return all(visited)
