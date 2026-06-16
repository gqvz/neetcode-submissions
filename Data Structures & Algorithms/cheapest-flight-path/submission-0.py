class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        m = defaultdict(list)
        for s, d, c in flights:
            m[s].append((c, d))
        q = [(0, 0, src)]
        visited = {}
        k += 1
        while q:
            c, s, v = heapq.heappop(q)
            # print("POP", v, "FROM THE HEAP")
            if v == dst:
                return c
            visited[v] = c
            if s < k:
                for ne in m[v]:
                    # print("PUT", ne[1], "IN THE HEAP")
                    heapq.heappush(q, (ne[0]+c, s+1, ne[1]))

        return -1
