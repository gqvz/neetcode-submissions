class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}
        for i in range(n):
            m[i] = []
        for edge in edges:
            m[edge[0]].append(edge[1])
            m[edge[1]].append(edge[0])
        visited = set()
        c = 0
        for i in range(n):
            if i not in visited:
                q = deque()
                q.append(i)
                while q:
                    k = q.popleft()
                    for neighbour in m[k]:
                        if neighbour not in visited:
                            q.append(neighbour)
                    visited.add(k)
                c += 1
        return c