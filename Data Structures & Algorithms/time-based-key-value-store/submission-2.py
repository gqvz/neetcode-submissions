from _bisect import bisect_left
class TimeMap:
    d: Dict[str, list[tuple[int, str]]]
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        index = bisect_left(self.d[key], timestamp, key=lambda x:x[0])
        self.d[key].insert(index, (timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        index = bisect_left(self.d[key], timestamp, key=lambda x:x[0])
        if index == len(self.d[key]) or self.d[key][index][0] != timestamp: index -= 1
        if index == -1: return ""
        return self.d[key][index][1]
