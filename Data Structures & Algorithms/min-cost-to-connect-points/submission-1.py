class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = [(1,2,3)]*(len(points)*(len(points)-1)//2)
        k = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges[k] = ((abs(points[i][0]-points[j][0])+abs(points[i][1] - points[j][1]), i, j))
                k += 1
        
        edges.sort()

        parent = [i for i in range(len(points))]
        size = [1 for i in range(len(points))]
        def findp(k: int):
            if k != parent[k]:
                parent[k] = findp(parent[k])
            return parent[k]
        
        def connect(u, v):
            u = findp(u)
            v = findp(v)
            if size[u] < size[v]:
                v, u = u, v
            parent[v] = u
            size[u] += size[v]
        
        cost = 0
        for d, i, j in edges:
            if findp(i) != findp(j):
                cost += d
                connect(i, j)

        return cost
