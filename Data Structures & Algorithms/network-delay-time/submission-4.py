class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(list)
        for s, d, t in times:
            m[s].append((d, t))
        
        visited = {}
        q = [(0, k)]
        while q:
            t, v = heapq.heappop(q)
            if v in visited: continue
            for ne in m[v]:
                heapq.heappush(q, (t+ne[1], ne[0]))
            visited[v] = t

        return max(visited.values()) if len(visited) == n else -1

