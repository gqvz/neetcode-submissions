class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for preq in prerequisites:
            m[preq[1]].append(preq[0])
        def dfs(curr, head, visited):
            if curr == head:
                return True
            visited.add(curr)
            # print("added ", curr, "to visited=", visited)
            for n in m[curr]:
                if n in visited or dfs(n, head, visited):
                    return True
            visited.remove(curr)
            # print("removed ", curr, "to visited=", visited)
            return False
        
        for i in range(numCourses):
            for n in m[i]:
                visited = set()
                if dfs(n, i, visited):
                    return False
        return True
