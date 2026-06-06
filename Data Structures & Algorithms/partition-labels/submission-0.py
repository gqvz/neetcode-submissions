class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i, c in enumerate(s):
            m[c] = i
        r = []
        mr = 0
        lmr = 0
        for i in range(len(s)):
            print(r, mr, lmr)
            if m[s[i]] > mr:
                mr = m[s[i]]
            if i == mr:
                r.append(mr-lmr)
                lmr = mr
        r[0] += 1
        return r



