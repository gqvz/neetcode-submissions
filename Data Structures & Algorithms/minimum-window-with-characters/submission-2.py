class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c = Counter(t)
        if t in s:
            return t
        start = next((i for i, x in enumerate(s) if x in t), 0) 
        print(c)
        print("Start is ", start)
        end = start
        c[s[start]] -= 1
        a = ""
        while (end := end + 1) < len(s):
            print("For end c = ", s[end])
            if s[end] in t:
                c[s[end]] -= 1
                print(c)
            if s[end] == s[start]:
                print("Moving Start from ", start)
                while start < len(s):
                    print("Start now at ", s[start])
                    if s[start] in c and c[s[start]] < 0:
                        c[s[start]] += 1
                        print(c)
                    elif s[start] in c and c[s[start]] == 0:
                        break
                    start += 1
            if (a == "" or len(a) > end - start) and all(map(lambda x: x<=0, c.values())):
                a = s[start:end+1]


        return a
