class CountSquares:

    def __init__(self):
        self.l = []

    def add(self, point: List[int]) -> None:
        self.l.append(point)

    def count(self, point: List[int]) -> int:
        sx = []
        sy = []
        sd = []
        for p in self.l:
            if p[0] == point[0] and p[1] == point[1]:
                # idk bruh
                continue
            if p[0] == point[0]:
                sx.append((point[1] - p[1], p))
            elif p[1] == point[1]:
                sy.append((point[0] - p[0], p))
            elif abs(p[1] - point[1]) == abs(p[0] - point[0]):
                sd.append((point[0] - p[0], point[1] - p[1], p))
        if not sx or not sy or not sd: return 0
        # print(sx, sy, sd)
        c = 0
        for dp in sd:
            nx = sum([1 for x in sx if x[0] == dp[1]])
            ny = sum([1 for y in sy if y[0] == dp[0]])
            c += nx * ny

        return c