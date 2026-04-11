class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        start = 0
        end = len(height) - 1
        sh = height[start]
        eh = height[end]
        waterlevel = min(sh, eh)
        water = min(sh, eh) * (end - start - 1)
        while start < end - 1:
            if sh <= eh:
                start += 1
                sh = height[start]
                water -= min(waterlevel, sh)
            else:
                end -= 1
                eh = height[end]
                water -= min(waterlevel, eh)
            water += max(0, min(sh, eh) - waterlevel) * (end - start - 1)
            waterlevel = max(waterlevel, min(sh, eh))
        return water
