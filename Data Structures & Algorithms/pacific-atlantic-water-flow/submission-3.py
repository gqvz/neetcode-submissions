class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        mi = len(heights[0])
        mj = len(heights)
        for i in range(mi):
            pacific.add((i, 0))
            atlantic.add((i, mj-1))
        for j in range(1, mj-1):
            pacific.add((0, j))
            atlantic.add((mi-1, j))
        pacific.add((0, mj-1))
        atlantic.add((mi-1, 0))

        q = deque(list(pacific))
        while q:
            i, j = q.popleft()
            if 0 <= j+1 < mj and heights[j+1][i] >= heights[j][i] and (i, j+1) not in pacific:
                pacific.add((i, j+1))
                q.append((i, j+1))
            if 0 <= i+1 < mi and heights[j][i+1] >= heights[j][i] and (i+1, j) not in pacific:
                pacific.add((i+1, j))
                q.append((i+1, j))
            if 0 <= i-1 < mi and (i-1, j) not in pacific and heights[j][i-1] >= heights[j][i]:
                pacific.add((i-1, j))
                q.append((i-1, j))
            if 0 <= i+1 < mi and (i+1, j) not in pacific and heights[j][i+1] >= heights[j][i]:
                pacific.add((i+1, j))
                q.append((i+1, j))

        q += list(atlantic)
        while q:
            i, j = q.popleft()
            if 0 <= j-1 < mj and heights[j-1][i] >= heights[j][i] and (i, j-1) not in atlantic:
                atlantic.add((i, j-1))
                q.append((i, j-1))
            if 0 <= i-1 < mi and heights[j][i-1] >= heights[j][i] and (i-1, j) not in atlantic:
                atlantic.add((i-1, j))
                q.append((i-1, j))
            if 0 <= i-1 < mi and (i-1, j) not in atlantic and heights[j][i-1] >= heights[j][i]:
                atlantic.add((i-1, j))
                q.append((i-1, j))
            if 0 <= i+1 < mi and (i+1, j) not in atlantic and heights[j][i+1] >= heights[j][i]:
                atlantic.add((i+1, j))
                q.append((i+1, j))
        print(pacific)
        print(atlantic)
        return [list(x)[::-1] for x in pacific.intersection(atlantic)]