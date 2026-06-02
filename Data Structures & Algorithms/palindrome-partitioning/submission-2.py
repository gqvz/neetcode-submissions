class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        for i in range(2**(len(s) - 1)):
            l = []
            num = 0
            lnum = -1
            while i:
                if i & 1 == 1:
                    v = ""
                    if num == 0:
                        v = s[-1]
                    else: 
                        if lnum == -1:
                            v = s[-num-1:]
                        else: v = s[-num-1:-lnum-1]
                    l.append(v)
                    lnum = num

                i >>= 1
                num += 1
            l.append(s[:-num if -num != 0 else None])
            # print(l)
            if all([y==y[::-1] for y in l]):
                res.append(l[::-1])

        return res
