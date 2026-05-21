from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        if t in s:
            return t
        
        c = Counter(t)
        need = len(c)
        
        start = next((i for i, x in enumerate(s) if x in c), -1)
        if start == -1:
            return ""
        
        end = start - 1
        a = ""
        
        while (end := end + 1) < len(s):
            ch = s[end]
            if ch in c:
                c[ch] -= 1
                if c[ch] == 0:
                    need -= 1
            
            while need == 0:
                if not a or end - start + 1 < len(a):
                    a = s[start:end + 1]
                sc = s[start]
                if sc in c:
                    c[sc] += 1
                    if c[sc] > 0:
                        need += 1
                start += 1
                while start <= end and s[start] not in c:
                    start += 1
        
        return a
