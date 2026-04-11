class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        start = 0
        end = len(height) - 1
        sh = height[start]
        eh = height[end]
        waterlevel = sh if sh < eh else eh 
        water = waterlevel * (end - start - 1)
        while start < end - 1:
            if sh <= eh:
                start += 1
                sh = height[start]
                water -= sh if sh < waterlevel else waterlevel  # ternary, no min()
            else:
                end -= 1
                eh = height[end]
                water -= eh if eh < waterlevel else waterlevel
            m = sh if sh < eh else eh
            delta = m - waterlevel
            if delta > 0:                          # branch skips multiply when flat
                water += delta * (end - start - 1)
                waterlevel = m 
        return water
