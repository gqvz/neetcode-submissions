class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = {}
        for i in range(n):
            m[i] = []
        for edge in edges:
            m[edge[0]].append(edge[1])
            m[edge[1]].append(edge[0])
        
        visited = set()
        q = deque([0])

        while q:
            k = q.popleft()
            if k in visited:
                return False
            for neighbour in m[k]:
                if neighbour not in visited:
                    q.append(neighbour)
            visited.add(k)
        return len(visited) == n