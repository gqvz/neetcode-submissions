class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i in range(len(s)):
            m[s[i]] = i
        r = []
        mr = lmr = 0
        for i in range(len(s)):
            mr = max(mr, m[s[i]])
            if i == mr:
                r.append(mr-lmr)
                lmr = mr
        r[0] += 1
        return r



