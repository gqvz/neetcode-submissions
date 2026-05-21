class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        if t in s:
            return t
        start = next((i for i, x in enumerate(s) if x in t), 0) 
        end = start
        c[s[start]] -= 1
        a = ""
        while (end := end + 1) < len(s):
            if s[end] in t:
                c[s[end]] -= 1
            if s[end] == s[start]:
                while start < len(s):
                    if s[start] in c and c[s[start]] < 0:
                        c[s[start]] += 1
                    elif s[start] in c and c[s[start]] == 0:
                        break
                    start += 1
            if (a == "" or len(a) > end - start) and all(map(lambda x: x<=0, c.values())):
                a = s[start:end+1]

        return a
