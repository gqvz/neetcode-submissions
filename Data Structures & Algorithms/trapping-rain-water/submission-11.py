class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        start = 0
        _min = min
        end = len(height) - 1
        sh = height[start]
        eh = height[end]
        waterlevel = _min(sh, eh)
        water = _min(sh, eh) * (end - start - 1)
        while start < end - 1:
            if sh <= eh:
                start += 1
                sh = height[start]
                water -= _min(waterlevel, sh)
            else:
                end -= 1
                eh = height[end]
                water -= _min(waterlevel, eh)
            delta = _min(sh, eh) - waterlevel
            if delta > 0:
                water += delta * (end - start - 1)
                waterlevel += delta
        return water
