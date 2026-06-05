class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for edge in edges:
            m[edge[0]].append(edge[1])
            m[edge[1]].append(edge[0])

        visited = []
        loop = set()
        found = False
        def dfs(root, parent):
            nonlocal found
            if found: return
            if root in visited:
                found = True
                last = visited.pop()
                while last != root:
                    loop.add(last)
                    last = visited.pop()
                loop.add(root)
                return
            visited.append(root)
            for n in m[root]:
                if n != parent:
                    dfs(n, root)
            if found: return
            visited.pop()
        dfs(1, -1)
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in loop and edges[i][1] in loop:
                return edges[i]
        return []
