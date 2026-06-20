class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        uniq = (set(''.join(words)))
        n = len(uniq)
        for i in range(1, len(words)):
            if words[i] in words[i-1] and len(words[i]) < len(words[i-1]): return ""
        edges = set()
        def buildgraph(cws):
            gs = groupby(cws, key=lambda x:x[0])
            last = None
            for k, g in gs:
                if last != None:
                    edges.add((last, k))
                last = k
                buildgraph([i[1:] for i in g if len(i) > 1])
        buildgraph(words)
        # print(edges)
        d = defaultdict(list)
        st = set()
        for edge in edges:
            d[edge[0]].append(edge[1])
            st.add(edge[1])
            
        
        visited = {}
        def checkloop(root): 
            if root in visited and visited[root]:
                return ""
            visited[root] = True
            for ne in d[root]:
                if checkloop(ne) == "": return ""
            visited[root] = False
            return "no"
        
        # print(edges)
        # print(uniq, st)
        start = (uniq-st).pop() if len(uniq-st) > 0 else words[0][0]
        if checkloop(start) == "": return ""
        ans = ""
        visited.clear()
        def dfs(root):
            nonlocal ans
            visited[root] = True
            for ne in d[root]:
                if ne not in visited:
                    dfs(ne)
            ans += (root)

        for i in uniq:
            if i not in visited:
                dfs(i)

        return ans[::-1]