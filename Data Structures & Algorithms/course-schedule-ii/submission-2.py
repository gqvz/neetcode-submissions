class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = defaultdict(list)
        for preq in prerequisites:
            m[preq[1]].append(preq[0])
        done = OrderedDict()
        def dfs(curr, head, visited, top):
            if curr == head and not top:
                return True
            visited.add(curr)
            # print("added ", curr, "to visited=", visited)
            for n in m[curr]:
                if n in visited or dfs(n, head, visited, False):
                    return True
            visited.remove(curr)
            done[curr] = True
            # print("removed ", curr, "to visited=", visited)
            return False
        
        for i in range(numCourses):
            if i not in done.keys():
                visited = set()
                if dfs(i, i, visited, True):
                    return []
        return list(done.keys())[::-1]
 