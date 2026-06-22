class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for t in tickets:
            d[t[0]].append(t[1])
        for (s, ds) in d.items():
            ds.sort(reverse=True)
        res = []
        def dfs(node):
            while d[node]:
                dfs(d[node].pop())
            res.append(node)
        dfs("JFK")
        
        return res[::-1]
