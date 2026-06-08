class Solution:
    def checkValidString(self, s: str) -> bool:
        k = k2 = 0
        for c in s:
            if c == "(" or c == "*":
                k += 1
            else:
                k -= 1
            if k < 0:
                return False
        
        for c in s[::-1]:
            if c == "(":
                k2 += 1
            else:
                k2 -= 1
            if k2 > 0:
                return False

        return True

# (((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)