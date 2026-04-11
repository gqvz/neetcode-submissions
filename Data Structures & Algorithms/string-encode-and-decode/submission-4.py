class Solution:

    def encode(self, strs: List[str]) -> str:
        s = f"{len(strs):2d}"
        for st in strs:
            s += f"{len(st):3d}{st}"
        return s

    def decode(self, s: str) -> List[str]:
        n = int(s[:2])
        strs = [""] * n
        start = 2
        for i in range(n):
            length = int(s[start:start+3])
            strs[i] = s[start+3:start+3+length]
            start += length + 3
        return strs
