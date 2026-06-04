class CountSquares:

    def __init__(self):
        self.l = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.l[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        c = 0
        for p, c1 in list(self.l.items()):
            if p[0] == point[0]:
                # print(p)
                d = p[1]-point[1]
                if d == 0: continue
                c += c1*self.l[(point[0]+d, point[1])]*self.l[(point[0]+d, p[1])]
                c += c1*self.l[(point[0]-d, point[1])]*self.l[(point[0]-d, p[1])]
        return c

