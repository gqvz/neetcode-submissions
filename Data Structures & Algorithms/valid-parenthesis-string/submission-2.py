class Solution:
    def checkValidString(self, s: str) -> bool:
        k = 0
        for c in s:
            if c == ")":
                k -= 1
            else:
                k += 1
            if k < 0:
                return False
        k = 0
        for i in range(len(s)-1, -1, -1):
            c = s[i]
            if c == "(":
                k += 1
            else:
                k -= 1
            if k > 0:
                return False

        return True

# (((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)