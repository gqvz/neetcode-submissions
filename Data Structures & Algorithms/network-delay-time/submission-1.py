class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        m = defaultdict(list)
        for s, d, t in times:
            m[s].append((d, t))
        
        visited = {}
        def dfs(root, time):
            if root in visited:
                if visited[root] <= time:
                    return
            visited[root] = time
            for n, t in m[root]:
                dfs(n, time+t)
                
        dfs(k, 0)
        # print(visited)
        return max(visited.values()) if len(visited) == n else -1
        
